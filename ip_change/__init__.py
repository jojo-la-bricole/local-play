import logging

from odoo import http

log = _logger = logging.getLogger(__name__)

log.info("IP CHANGE LOADED")


class IPChangeController(http.Controller):

    @http.route('/_odoo.sh/ip-change', auth='public')
    def ip_change(self, old=None, new=None):
        _logger.info("IP address changed from %s to %s", old, new)
        # Then perform whatever action required for your use-case, eg: update an
        # ir.config_parameter, send an email, contact an external firewall service's API, ...
        return 'ok'
