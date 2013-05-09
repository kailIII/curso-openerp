from osv import osv, fields

class indicador(osv.Model):
    _name = 'evalunl.indicador'
    _columns = {
        'nombre' = fields.char('Nombre', required=True, translate=True),
        'valor' = fields.float('Valor', digits=(3,1))
        }
