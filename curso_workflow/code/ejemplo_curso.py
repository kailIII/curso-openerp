# -*- coding: utf-8 -*-
###################################################
#
#    BUILDING CRM Module
#    Copyright (C) 2011-2011 Atikasoft Cia.Ltda. (<http://www.atikasoft.com.ec>).
#    $autor: Katherine Robles Arévalo<katy.robles@atikasoft.com.ec>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################


from osv import osv, fields
from ..constants import _STATES_CURSO

class curso_example(osv.osv):
    # Es otro objeto del modelo, no es el objeto curso del modulo curso_code
    _name ="course.example"
    _table = "course_example"
    _description = "Tabla de Ejemplos"
    
    _columns = {
                'name':fields.char('Nombre',size=64),
                'student':fields.many2one('curso.alumno','Alumno'),
                'teacher':fields.many2one('curso.profesor','Profesor'),
                'description':fields.text('Descripción'),
                # Todos los estados que se pueden manejar en este objeto
                'state':fields.selection(_STATES_CURSO,string="Estado", readonly=True)
                }

    _defaults = {  
                'state': lambda *a: 'draft'
                }

curso_example()

class curso_alumno(osv.osv):
    _name = 'curso.alumno'
    _inherit = 'curso.alumno'
    _columns = {
        'direccion':fields.char('Direccion', size=64)
        }
