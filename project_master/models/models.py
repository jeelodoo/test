# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_master(models.Model):
	_inherit = "project.project"


	cabang_id = fields.Many2one('res.branch','Cabang')
	# cabang_id = fields.Selection([('jakarta', 'Jakarta'),('bali', 'Bali'), ('surabaya', 'Surabaya'), ('batam', 'Batam')], string="Cabang")
	id_proyek = fields.Char("ID Proyek")
	nama_proyek = fields.Char("Nama Proyek")
	nilai_kontrak = fields.Float("Nilai Kontrak")
	nilai_persen = fields.Float("Nilai Persen")
	nilai_uang_muka = fields.Float("Nilai Uang Muka")
	
	nama_owner_id = fields.Many2one('res.partner', string="Nama Owner", domain="[('customer', '=', True)]")
	npwp_owner = fields.Char(related="nama_owner_id.npwp", string="NPWP Owner")
	alamat_owner = fields.Char(related='nama_owner_id.street' ,string="Alamat Owner")
	street2 = fields.Char(related='nama_owner_id.street2')
	city = fields.Char(related='nama_owner_id.city', string="City")
	state_id = fields.Many2one(related='nama_owner_id.state_id')
	zipp = fields.Char(related='nama_owner_id.zip')
	country_id = fields.Many2one(related='nama_owner_id.country_id' ,string="Country")
	project_manager_id = fields.Many2many('res.users', string="Project Manager")
	nama_od_id = fields.Many2many('res.users', string="Nama OD")
	project_ko_id = fields.Many2many('res.users', string="Project Koordinator")
	qs_user_id = fields.Many2many('res.users', string="QS User")
	income_account_id = fields.Many2one('account.account', string="Income Account")

	@api.onchange('nilai_kontrak', 'nilai_persen')
	def _calculate_nilai_uang_muka(self):
		for rec in self:
			if rec.nilai_kontrak and rec.nilai_persen:
				rec.nilai_uang_muka = rec.nilai_kontrak * rec.nilai_persen / 100

	# @api.onchange('nilai_kontrak', 'nilai_uang_muka')
	# def _calculate_nilai_persen(self):
	# 	for rec in self:
	# 		if rec.nilai_kontrak and rec.nilai_uang_muka:
	# 			rec.nilai_persen = rec.nilai_uang_muka * 100 / rec.nilai_kontrak
