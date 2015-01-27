# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields

class account_voucher_line(osv.osv):
	_inherit = 'account.voucher.line'


	def _check_original_amount(self, cr, uid, ids, context=None):
	        obj = self.browse(cr, uid, ids[0], context=context)
        	if obj.amount > obj.amount_original:
	        	return False
        	return True

	_constraints = [
        	(_check_original_amount, 'Amount should not exceed original_amount.', ['amount']),
	    ]

account_voucher_line()
