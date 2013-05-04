from osv import osv, fields 
class alumno(osv.osv):
    _name = 'curso.alumno'

    def _get_num_creditos(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        materia_class = self.pool.get('curso.materia')
        # Seleccionar todos
        # search() me devuelve los ids de los registros
        materia_ids = materia_class.search(cr, uid, [])
        materias = materia_class.browse(cr, uid, materia_ids)
        total_creditos = 0
        for m in materias:
            total_creditos += m.creditos

        # TODO: Se deberia mejorar en base a las relaciones
        alumnos = self.browse(cr, uid, ids, context=context)
        for alum in alumnos:
            res[alum.id] = total_creditos
        return res

    _columns = {
          'name':fields.char('nombre', size=64),
          'cedula':fields.char('ced', size=10),
          'edad':fields.integer('Edad'),
          'curso_id':fields.many2one('curso.curso', 'Curso'),
          #'profesor_id':fields.many2one('curso.profesor', 'Profesor'),
	  'materia_ids':fields.many2many('curso.materia','alumno_materia_rel',
                                         'alumno_id','materia_id','materias'),
          'num_creditos': fields.function(_get_num_creditos, string="Credito",
                                          method=True, store=False, 
                                          type='integer')
    }
alumno()
