
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

import prefix_limit
import config
import state
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 unicast configuration options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix_limit','__config','__state',)

  _yang_name = 'ipv4-unicast'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast']

  def _get_prefix_limit(self):
    """
    Getter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/prefix_limit (container)

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    return self.__prefix_limit
      
  def _set_prefix_limit(self, v, load=False):
    """
    Setter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/prefix_limit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_limit() directly.

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_limit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__prefix_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_limit(self):
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config (container)

    YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/state (container)

    YANG Description: State information for common IPv4 and IPv6 unicast
parameters
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State information for common IPv4 and IPv6 unicast
parameters
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

  prefix_limit = __builtin__.property(_get_prefix_limit, _set_prefix_limit)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'prefix_limit': prefix_limit, 'config': config, 'state': state, }


import prefix_limit
import config
import state
class ipv4_unicast(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/afi-safis/afi-safi/ipv4-unicast. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: IPv4 unicast configuration options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__prefix_limit','__config','__state',)

  _yang_name = 'ipv4-unicast'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'bgp', u'neighbors', u'neighbor', u'afi-safis', u'afi-safi', u'ipv4-unicast']

  def _get_prefix_limit(self):
    """
    Getter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/prefix_limit (container)

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    return self.__prefix_limit
      
  def _set_prefix_limit(self, v, load=False):
    """
    Setter method for prefix_limit, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/prefix_limit (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_limit() directly.

    YANG Description: Configure the maximum number of prefixes that will be
accepted from a peer
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_limit must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
        })

    self.__prefix_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_limit(self):
    self.__prefix_limit = YANGDynClass(base=prefix_limit.prefix_limit, is_container='container', yang_name="prefix-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config (container)

    YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters for common IPv4 and IPv6 unicast
AFI-SAFI options
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/state (container)

    YANG Description: State information for common IPv4 and IPv6 unicast
parameters
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/afi_safis/afi_safi/ipv4_unicast/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State information for common IPv4 and IPv6 unicast
parameters
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

  prefix_limit = __builtin__.property(_get_prefix_limit, _set_prefix_limit)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = {'prefix_limit': prefix_limit, 'config': config, 'state': state, }


