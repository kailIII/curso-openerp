from osv import  osv, fields
class profesor(osv.osv):
  _name='curso.profesor'
  _columns= {
 'name':fields.char('nombre',size=32),
 'code': fields.char('cod',size=8),
 'edad':fields.integer('Edad'),
 'alumno_ids':fields.one2many('curso.alumno', 'profesor_id', 'Alumnos'),
 'materia_ids':fields.one2many('curso.materia', 'profesor_id', 'Materias'),
    
             }
profesor()