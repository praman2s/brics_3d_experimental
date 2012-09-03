"""autogenerated by genmsg_py from AddNodeRequest.msg. Do not edit."""
import roslib.message
import struct

import brics_3d_msgs.msg

class AddNodeRequest(roslib.message.Message):
  _md5sum = "601e6827130e51a02c18d101adf4e480"
  _type = "brics_3d_msgs/AddNodeRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
uint32 parentId
Attribute[] attributes

================================================================================
MSG: brics_3d_msgs/Attribute
# Attribute description for objects in the world model
string key
string value
"""
  __slots__ = ['parentId','attributes']
  _slot_types = ['uint32','brics_3d_msgs/Attribute[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       parentId,attributes
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(AddNodeRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.parentId is None:
        self.parentId = 0
      if self.attributes is None:
        self.attributes = []
    else:
      self.parentId = 0
      self.attributes = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      buff.write(_struct_I.pack(self.parentId))
      length = len(self.attributes)
      buff.write(_struct_I.pack(length))
      for val1 in self.attributes:
        _x = val1.key
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (self.parentId,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.attributes = []
      for i in range(0, length):
        val1 = brics_3d_msgs.msg.Attribute()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.value = str[start:end]
        self.attributes.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      buff.write(_struct_I.pack(self.parentId))
      length = len(self.attributes)
      buff.write(_struct_I.pack(length))
      for val1 in self.attributes:
        _x = val1.key
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.value
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.parentId,) = _struct_I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.attributes = []
      for i in range(0, length):
        val1 = brics_3d_msgs.msg.Attribute()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.key = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        val1.value = str[start:end]
        self.attributes.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
"""autogenerated by genmsg_py from AddNodeResponse.msg. Do not edit."""
import roslib.message
import struct


class AddNodeResponse(roslib.message.Message):
  _md5sum = "b61aa853c722cf9ad83045ec5f1f777a"
  _type = "brics_3d_msgs/AddNodeResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 assignedId
bool succeeded


"""
  __slots__ = ['assignedId','succeeded']
  _slot_types = ['uint32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       assignedId,succeeded
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(AddNodeResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.assignedId is None:
        self.assignedId = 0
      if self.succeeded is None:
        self.succeeded = False
    else:
      self.assignedId = 0
      self.succeeded = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_IB.pack(_x.assignedId, _x.succeeded))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.assignedId, _x.succeeded,) = _struct_IB.unpack(str[start:end])
      self.succeeded = bool(self.succeeded)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_IB.pack(_x.assignedId, _x.succeeded))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.assignedId, _x.succeeded,) = _struct_IB.unpack(str[start:end])
      self.succeeded = bool(self.succeeded)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_IB = struct.Struct("<IB")
class AddNode(roslib.message.ServiceDefinition):
  _type          = 'brics_3d_msgs/AddNode'
  _md5sum = '6eade559b409ccbd98ecfb3aa854fb1c'
  _request_class  = AddNodeRequest
  _response_class = AddNodeResponse
