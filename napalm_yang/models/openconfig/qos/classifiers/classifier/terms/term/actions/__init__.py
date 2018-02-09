
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

from . import config
from . import state
from . import remark
class actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos - based on the path /qos/classifiers/classifier/terms/term/actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Actions to be applied for packets matching the specified
classification rules.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__remark',)

  _yang_name = 'actions'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__remark = YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'qos', u'classifiers', u'classifier', u'terms', u'term', u'actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/config (container)

    YANG Description: Actions to be applied to packets that match the classifier
term.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Actions to be applied to packets that match the classifier
term.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state (container)

    YANG Description: Operational state parameters associated with classifier term
actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters associated with classifier term
actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_remark(self):
    """
    Getter method for remark, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/remark (container)

    YANG Description: Remark actions to be associated with packets that match the
classifier term. Where a packet matches these criteria, the
specified rewrite actions should be performed.
    """
    return self.__remark
      
  def _set_remark(self, v, load=False):
    """
    Setter method for remark, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/remark (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remark() directly.

    YANG Description: Remark actions to be associated with packets that match the
classifier term. Where a packet matches these criteria, the
specified rewrite actions should be performed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remark must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remark(self):
    self.__remark = YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  remark = __builtin__.property(_get_remark, _set_remark)


  _pyangbind_elements = {'config': config, 'state': state, 'remark': remark, }


from . import config
from . import state
from . import remark
class actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-interfaces - based on the path /qos/classifiers/classifier/terms/term/actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Actions to be applied for packets matching the specified
classification rules.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__remark',)

  _yang_name = 'actions'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__remark = YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'qos', u'classifiers', u'classifier', u'terms', u'term', u'actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/config (container)

    YANG Description: Actions to be applied to packets that match the classifier
term.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Actions to be applied to packets that match the classifier
term.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state (container)

    YANG Description: Operational state parameters associated with classifier term
actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters associated with classifier term
actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_remark(self):
    """
    Getter method for remark, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/remark (container)

    YANG Description: Remark actions to be associated with packets that match the
classifier term. Where a packet matches these criteria, the
specified rewrite actions should be performed.
    """
    return self.__remark
      
  def _set_remark(self, v, load=False):
    """
    Setter method for remark, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/remark (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remark() directly.

    YANG Description: Remark actions to be associated with packets that match the
classifier term. Where a packet matches these criteria, the
specified rewrite actions should be performed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remark must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remark(self):
    self.__remark = YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  remark = __builtin__.property(_get_remark, _set_remark)


  _pyangbind_elements = {'config': config, 'state': state, 'remark': remark, }


from . import config
from . import state
from . import remark
class actions(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-qos-elements - based on the path /qos/classifiers/classifier/terms/term/actions. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Actions to be applied for packets matching the specified
classification rules.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__remark',)

  _yang_name = 'actions'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    self.__remark = YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'qos', u'classifiers', u'classifier', u'terms', u'term', u'actions']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/config (container)

    YANG Description: Actions to be applied to packets that match the classifier
term.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Actions to be applied to packets that match the classifier
term.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state (container)

    YANG Description: Operational state parameters associated with classifier term
actions
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state parameters associated with classifier term
actions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)


  def _get_remark(self):
    """
    Getter method for remark, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/remark (container)

    YANG Description: Remark actions to be associated with packets that match the
classifier term. Where a packet matches these criteria, the
specified rewrite actions should be performed.
    """
    return self.__remark
      
  def _set_remark(self, v, load=False):
    """
    Setter method for remark, mapped from YANG variable /qos/classifiers/classifier/terms/term/actions/remark (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remark is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remark() directly.

    YANG Description: Remark actions to be associated with packets that match the
classifier term. Where a packet matches these criteria, the
specified rewrite actions should be performed.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remark must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)""",
        })

    self.__remark = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remark(self):
    self.__remark = YANGDynClass(base=remark.remark, is_container='container', yang_name="remark", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/qos', defining_module='openconfig-qos', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  remark = __builtin__.property(_get_remark, _set_remark)


  _pyangbind_elements = {'config': config, 'state': state, 'remark': remark, }


