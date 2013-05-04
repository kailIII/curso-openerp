'''
Created on 03/05/2013

@author: miltonlab
'''
from osv import osv, fields
class curso_materia(osv.osv):
    _name = 'curso.materia'
    _columns = {
          'name':fields.char('nombre', size=64),
          #tiene que ser name
          'descripcion':fields.text('Descripcion'),
          'horas':fields.integer('Horas'),
          'creditos':fields.float('Creditos', digits=(2,1)),
          #atributo name de la clase del modelo One
          'profesor_id':fields.many2one('curso.profesor','Profesor'),
          # TODO
	  #'alumnos_ids':fields.many2many('curso.alumno','alumno_materia_rel','materia_id','alumno_id','alumnos'),

          
    }

    def create(self, cr, uid, vals, context=None):
        print 'mi create', vals
        creditos = vals['creditos']
        if creditos > 32:
            raise osv.except_osv(('Invalid'), ('No puede ser mayor a 32'))
        # Se obtiene una instancia???
        # Mas bien parece que se obtiene la clase
        profesor_obj = self.pool.get('curso.profesor')
        # Las operadores en los criterios de busqueda puede ser 
        # cualquiera de los soportados en la clausula WHERE de SQL
        profesor_ids = profesor_obj.search(cr, uid, [('code','=','001')])
        # Todos los objetos profesor que cumplen con la condicion
        profesores_data = profesor_obj.browse(cr, uid, profesor_ids)
        for profe in profesores_data:
            print profe.name
            print 'Sus alumnos son:'
            #En la version del profesor
            #alumnos_data = profe.alumno_ids
            materias_data = profe.materia_ids
            for mat in materias_data:
                alumnos_data = mat.alumno_ids
                for alum in alumnos_data:
                    print alum.name
            
        return super(curso_materia, self).create(cr, uid, vals, context)
    
    def on_change_creditos(self, cr, uid, ids, num_creditos):
        """
        Despues de ids vienen todos los parametros que llegan desde la vista
        """
        print 'num_creditos: ', num_creditos
        if not num_creditos:
            return False
        if num_creditos > 32:
            raise osv.except_osv(('Invalid'), ('No puede ser mayor a 32'))
        return True

curso_materia()
