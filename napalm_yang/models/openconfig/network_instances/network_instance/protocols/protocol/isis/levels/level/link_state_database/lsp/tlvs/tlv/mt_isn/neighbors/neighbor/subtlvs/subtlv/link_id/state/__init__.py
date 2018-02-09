
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

class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/subtlvs/subtlv/link-id/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of sub-TLV 4.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_','__remote',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__remote = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isn', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'link-id', u'state']

  def _get_local_(self):
    """
    Getter method for local_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/local (uint32)

    YANG Description: The value field of this sub-TLV contains 4 octets of
Link Local Identifier followed by 4 octets of Link
Remote Identifier.
    """
    return self.__local_
      
  def _set_local_(self, v, load=False):
    """
    Setter method for local_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/local (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_() directly.

    YANG Description: The value field of this sub-TLV contains 4 octets of
Link Local Identifier followed by 4 octets of Link
Remote Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__local_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_(self):
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_remote(self):
    """
    Getter method for remote, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/remote (uint32)

    YANG Description: If the Link Remote Identifier is unknown, it is set
to 0.
    """
    return self.__remote
      
  def _set_remote(self, v, load=False):
    """
    Setter method for remote, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/remote (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote() directly.

    YANG Description: If the Link Remote Identifier is unknown, it is set
to 0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote(self):
    self.__remote = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  local_ = __builtin__.property(_get_local_)
  remote = __builtin__.property(_get_remote)


  _pyangbind_elements = {'local_': local_, 'remote': remote, }


class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn/neighbors/neighbor/subtlvs/subtlv/link-id/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of sub-TLV 4.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__local_','__remote',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    self.__remote = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'mt-isn', u'neighbors', u'neighbor', u'subtlvs', u'subtlv', u'link-id', u'state']

  def _get_local_(self):
    """
    Getter method for local_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/local (uint32)

    YANG Description: The value field of this sub-TLV contains 4 octets of
Link Local Identifier followed by 4 octets of Link
Remote Identifier.
    """
    return self.__local_
      
  def _set_local_(self, v, load=False):
    """
    Setter method for local_, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/local (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_() directly.

    YANG Description: The value field of this sub-TLV contains 4 octets of
Link Local Identifier followed by 4 octets of Link
Remote Identifier.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_ must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__local_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_(self):
    self.__local_ = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)


  def _get_remote(self):
    """
    Getter method for remote, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/remote (uint32)

    YANG Description: If the Link Remote Identifier is unknown, it is set
to 0.
    """
    return self.__remote
      
  def _set_remote(self, v, load=False):
    """
    Setter method for remote, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors/neighbor/subtlvs/subtlv/link_id/state/remote (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote() directly.

    YANG Description: If the Link Remote Identifier is unknown, it is set
to 0.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)""",
        })

    self.__remote = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote(self):
    self.__remote = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=False)

  local_ = __builtin__.property(_get_local_)
  remote = __builtin__.property(_get_remote)


  _pyangbind_elements = {'local_': local_, 'remote': remote, }


