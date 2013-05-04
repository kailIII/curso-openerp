from osv import osv, fields
class curso(osv.osv):
    _name = 'curso.curso'
    _columns = {
        'name': fields.char('nombre', size=64),
        'code': fields.char('codigo', size=10),
        'fecha_inicio': fields.date('Fecha Inicio'),
        'alumno_ids':fields.one2many('curso.alumno', 'curso_id', 'Alumnos'),
                        
    }
curso()
