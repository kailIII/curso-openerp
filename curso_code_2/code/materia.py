from osv import osv, fields
class curso_materia(osv.osv):
    _name = 'curso.materia'
    _columns = {
        'name': fields.char('nombre', size=64),
        'horas': fields.integer('Horas'),
        'creditos': fields.integer('Creditos'),
        'descripcion':fields.text('Descripcion'),
        #'fecha_inicio': fields.date('Fecha Inicio'),
        #'alumno_ids':fields.one2many('curso.alumno', 'curso_id', 'Alumnos'),
        'profesor_id':fields.many2one('curso.profesor', 'Profesor'),
                        
    }
     
    
    
curso_materia()