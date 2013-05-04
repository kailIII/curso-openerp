# -*- coding: utf-8 -*-
###################################################
#
#    Curso Coviprov
#    Copyright (C) 2012 Atikasoft Cia.Ltda. (<http://www.atikasoft.com.ec>).
#    $autor: Dairon Medina Caro <dairon.medina@gmail.com>
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

{
    "name" : "Capacitacion OPenERP",
    "version" : "1.0",
    "depends" : [],
    'author': 'Vassis S.A.',
    "category": "Generic Modules/Human Resources",
    'website': 'http://vassisecuador.wordpress.com',
    'description': 
                    """
                    Módulo de Evaluacion de la capacitacion a los empleados publicos
                    """,
    'init_xml': [],
    'update_xml': [
               #"security/ir.model.access.csv",
               "views/profesor_view.xml",
               "views/alumno_view.xml",
               "views/materia.xml",
               "views/menu_items.xml",
               
               #"views/capacitacion_evaluacion_view.xml",
               #"views/evaluacion_view.xml",
               #"views/solicitud_evaluacion_view.xml",
               #"views/menu_items.xml",
               
    ],
    'installable': True,
    'active': False,
}
