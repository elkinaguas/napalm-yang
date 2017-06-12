
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
import __builtin__
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
 long = int
 unicode = str

import config
import state
import interface_attributes
import reserved_label_blocks
class global_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: general mpls configuration applicable to any
type of LSP and signaling protocol - label ranges,
entropy label supportmay be added here
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__interface_attributes','__reserved_label_blocks',)

  _yang_name = 'global'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reserved_label_blocks = YANGDynClass(base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/global/config (container)

    YANG Description: Top level global MPLS configuration
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/global/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Top level global MPLS configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/global/state (container)

    YANG Description: Top level global MPLS state
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Top level global MPLS state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interface_attributes(self):
    """
    Getter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes (container)

    YANG Description: Parameters related to MPLS interfaces
    """
    return self.__interface_attributes
      
  def _set_interface_attributes(self, v, load=False):
    """
    Setter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_attributes() directly.

    YANG Description: Parameters related to MPLS interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interface_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_attributes(self):
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_reserved_label_blocks(self):
    """
    Getter method for reserved_label_blocks, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks (container)

    YANG Description: A range of labels starting with the start-label and up-to and including
the end label that should be allocated as reserved. These labels should
not be utilised by any dynamic label allocation on the local system unless
the allocating protocol is explicitly configured to specify that
allocation of labels should be out of the label block specified.
    """
    return self.__reserved_label_blocks
      
  def _set_reserved_label_blocks(self, v, load=False):
    """
    Setter method for reserved_label_blocks, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reserved_label_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reserved_label_blocks() directly.

    YANG Description: A range of labels starting with the start-label and up-to and including
the end label that should be allocated as reserved. These labels should
not be utilised by any dynamic label allocation on the local system unless
the allocating protocol is explicitly configured to specify that
allocation of labels should be out of the label block specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reserved_label_blocks must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__reserved_label_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reserved_label_blocks(self):
    self.__reserved_label_blocks = YANGDynClass(base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  interface_attributes = __builtin__.property(_get_interface_attributes, _set_interface_attributes)
  reserved_label_blocks = __builtin__.property(_get_reserved_label_blocks, _set_reserved_label_blocks)


  _pyangbind_elements = {'config': config, 'state': state, 'interface_attributes': interface_attributes, 'reserved_label_blocks': reserved_label_blocks, }


import config
import state
import interface_attributes
import reserved_label_blocks
class global_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: general mpls configuration applicable to any
type of LSP and signaling protocol - label ranges,
entropy label supportmay be added here
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__config','__state','__interface_attributes','__reserved_label_blocks',)

  _yang_name = 'global'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__reserved_label_blocks = YANGDynClass(base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'mpls', u'global']

  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/global/config (container)

    YANG Description: Top level global MPLS configuration
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/global/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Top level global MPLS configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/global/state (container)

    YANG Description: Top level global MPLS state
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Top level global MPLS state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_interface_attributes(self):
    """
    Getter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes (container)

    YANG Description: Parameters related to MPLS interfaces
    """
    return self.__interface_attributes
      
  def _set_interface_attributes(self, v, load=False):
    """
    Setter method for interface_attributes, mapped from YANG variable /network_instances/network_instance/mpls/global/interface_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_attributes() directly.

    YANG Description: Parameters related to MPLS interfaces
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__interface_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_attributes(self):
    self.__interface_attributes = YANGDynClass(base=interface_attributes.interface_attributes, is_container='container', yang_name="interface-attributes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_reserved_label_blocks(self):
    """
    Getter method for reserved_label_blocks, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks (container)

    YANG Description: A range of labels starting with the start-label and up-to and including
the end label that should be allocated as reserved. These labels should
not be utilised by any dynamic label allocation on the local system unless
the allocating protocol is explicitly configured to specify that
allocation of labels should be out of the label block specified.
    """
    return self.__reserved_label_blocks
      
  def _set_reserved_label_blocks(self, v, load=False):
    """
    Setter method for reserved_label_blocks, mapped from YANG variable /network_instances/network_instance/mpls/global/reserved_label_blocks (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reserved_label_blocks is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reserved_label_blocks() directly.

    YANG Description: A range of labels starting with the start-label and up-to and including
the end label that should be allocated as reserved. These labels should
not be utilised by any dynamic label allocation on the local system unless
the allocating protocol is explicitly configured to specify that
allocation of labels should be out of the label block specified.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reserved_label_blocks must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__reserved_label_blocks = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reserved_label_blocks(self):
    self.__reserved_label_blocks = YANGDynClass(base=reserved_label_blocks.reserved_label_blocks, is_container='container', yang_name="reserved-label-blocks", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)
  interface_attributes = __builtin__.property(_get_interface_attributes, _set_interface_attributes)
  reserved_label_blocks = __builtin__.property(_get_reserved_label_blocks, _set_reserved_label_blocks)


  _pyangbind_elements = {'config': config, 'state': state, 'interface_attributes': interface_attributes, 'reserved_label_blocks': reserved_label_blocks, }


