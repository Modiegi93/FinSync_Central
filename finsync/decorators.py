from django.http import HttpResponseRedirect
from finsync import utils


def custom_login_required(view_func):
    """Custom login required"""
    def wrapper(request, *args, **kw):
        # Collect alerts
        alerts = utils.get_alerts(request)

        # Require login
        if not request.user.is_authenticated:
            alerts.append(('info', 'Oops!', 'You have not logged in...'))
            request.session['alerts'] = alerts
            return HttpResponseRedirect('/accounts/login')

        data = {'alerts': alerts}
        return view_func(request, data, *args, **kw)

    return wrapper
