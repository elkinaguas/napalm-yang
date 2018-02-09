
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

from . import ipv6_srlg
class ipv6_srlgs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv6-srlgs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS SRLG TLV.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ipv6_srlg',)

  _yang_name = 'ipv6-srlgs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ipv6_srlg = YANGDynClass(base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'ipv6-srlgs']

  def _get_ipv6_srlg(self):
    """
    Getter method for ipv6_srlg, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv6_srlgs/ipv6_srlg (list)

    YANG Description: Instance of the IPv6 SRLG TLV.
    """
    return self.__ipv6_srlg
      
  def _set_ipv6_srlg(self, v, load=False):
    """
    Setter method for ipv6_srlg, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv6_srlgs/ipv6_srlg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_srlg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_srlg() directly.

    YANG Description: Instance of the IPv6 SRLG TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_srlg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__ipv6_srlg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_srlg(self):
    self.__ipv6_srlg = YANGDynClass(base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  ipv6_srlg = __builtin__.property(_get_ipv6_srlg)


  _pyangbind_elements = {'ipv6_srlg': ipv6_srlg, }


from . import ipv6_srlg
class ipv6_srlgs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv6-srlgs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS SRLG TLV.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__ipv6_srlg',)

  _yang_name = 'ipv6-srlgs'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ipv6_srlg = YANGDynClass(base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

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
      return [u'network-instances', u'network-instance', u'protocols', u'protocol', u'isis', u'levels', u'level', u'link-state-database', u'lsp', u'tlvs', u'tlv', u'ipv6-srlgs']

  def _get_ipv6_srlg(self):
    """
    Getter method for ipv6_srlg, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv6_srlgs/ipv6_srlg (list)

    YANG Description: Instance of the IPv6 SRLG TLV.
    """
    return self.__ipv6_srlg
      
  def _set_ipv6_srlg(self, v, load=False):
    """
    Setter method for ipv6_srlg, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv6_srlgs/ipv6_srlg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_srlg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_srlg() directly.

    YANG Description: Instance of the IPv6 SRLG TLV.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_srlg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
        })

    self.__ipv6_srlg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_srlg(self):
    self.__ipv6_srlg = YANGDynClass(base=YANGListType("instance_number",ipv6_srlg.ipv6_srlg, yang_name="ipv6-srlg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-number', extensions=None), is_container='list', yang_name="ipv6-srlg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)

  ipv6_srlg = __builtin__.property(_get_ipv6_srlg)


  _pyangbind_elements = {'ipv6_srlg': ipv6_srlg, }


