Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/coercions.py", line 530, in _literal_coercion
    return expr._bind_param(operator, element, type_=bindparam_type)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/elements.py", line 4734, in _bind_param
    return BindParameter(
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/elements.py", line 1565, in __init__
    self.type = _compared_to_type.coerce_compared_value(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/type_api.py", line 791, in coerce_compared_value
    _coerced_type = _resolve_value_to_type(value)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/sqltypes.py", line 3362, in _resolve_value_to_type
    raise exc.ArgumentError(
sqlalchemy.exc.ArgumentError: Object <models.Usuario object at 0x7bbc0cef7a40> is not legal as a SQL literal value

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/lib/python3.12/tkinter/__init__.py", line 1967, in __call__
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "/home/steve/orm_sql_alchemy.py", line 143, in autenticar
    abrir_gestor_archivos(rol_usuario)
  File "/home/steve/orm_sql_alchemy.py", line 121, in abrir_gestor_archivos
    funciones_db = obtener_funciones_rol(session, rol_usuario)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/steve/functions.py", line 40, in obtener_funciones_rol
    funciones = session.query(Funcion).join(FuncionesRol).filter(FuncionesRol.id_rol == id_rol).all()
                                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/operators.py", line 387, in __eq__
    return self.operate(eq, other)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/orm/attributes.py", line 322, in operate
    return op(self.comparator, *other, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/operators.py", line 387, in __eq__
    return self.operate(eq, other)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/orm/properties.py", line 426, in operate
    return op(self.__clause_element__(), *other, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/annotation.py", line 225, in __eq__
    return self.__element.__class__.__eq__(self, other)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/operators.py", line 387, in __eq__
    return self.operate(eq, other)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/elements.py", line 873, in operate
    return op(self.comparator, *other, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/operators.py", line 387, in __eq__
    return self.operate(eq, other)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/type_api.py", line 77, in operate
    return o[0](self.expr, op, *(other + o[1:]), **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/default_comparator.py", line 101, in _boolean_compare
    obj = coercions.expect(
          ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/coercions.py", line 193, in expect
    resolved = impl._literal_coercion(
               ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/coercions.py", line 532, in _literal_coercion
    self._raise_for_expected(element, err=err)
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/coercions.py", line 517, in _raise_for_expected
    return super(ExpressionElementImpl, self)._raise_for_expected(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/sqlalchemy/sql/coercions.py", line 290, in _raise_for_expected
    util.raise_(exc.ArgumentError(msg, code=code), replace_context=err)
  File "/usr/lib/python3/dist-packages/sqlalchemy/util/compat.py", line 211, in raise_
    raise exception
sqlalchemy.exc.ArgumentError: SQL expression element or literal value expected, got <models.Usuario object at 0x7bbc0cef7a40>.
^CTraceback (most recent call last):
  File "/home/steve/orm_sql_alchemy.py", line 173, in <module>
    root.mainloop()
  File "/usr/lib/python3.12/tkinter/__init__.py", line 1504, in mainloop
    self.tk.mainloop(n)
