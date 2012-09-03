"""autogenerated by genmsg_py from GetSceneObjectsRequest.msg. Do not edit."""
import roslib.message
import struct

import brics_3d_msgs.msg

class GetSceneObjectsRequest(roslib.message.Message):
  _md5sum = "7aeaec9af856796f8fbf7690da21da2f"
  _type = "brics_3d_msgs/GetSceneObjectsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Attribute[] attributes

================================================================================
MSG: brics_3d_msgs/Attribute
# Attribute description for objects in the world model
string key
string value
"""
  __slots__ = ['attributes']
  _slot_types = ['brics_3d_msgs/Attribute[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       attributes
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GetSceneObjectsRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.attributes is None:
        self.attributes = []
    else:
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
"""autogenerated by genmsg_py from GetSceneObjectsResponse.msg. Do not edit."""
import roslib.message
import struct

import arm_navigation_msgs.msg
import geometry_msgs.msg
import brics_3d_msgs.msg
import std_msgs.msg

class GetSceneObjectsResponse(roslib.message.Message):
  _md5sum = "9575eab9a485984c889841a7b7bf0b22"
  _type = "brics_3d_msgs/GetSceneObjectsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """SceneObject[] results

================================================================================
MSG: brics_3d_msgs/SceneObject
# Description of an object in the world model
uint32 id
uint32 parentId
geometry_msgs/TransformStamped transform
arm_navigation_msgs/Shape shape 
Attribute[] attributes

================================================================================
MSG: geometry_msgs/TransformStamped
# This expresses a transform from coordinate frame header.frame_id
# to the coordinate frame child_frame_id
#
# This message is mostly used by the 
# <a href="http://www.ros.org/wiki/tf">tf</a> package. 
# See it's documentation for more information.

Header header
string child_frame_id # the frame id of the child frame
Transform transform

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: arm_navigation_msgs/Shape
byte SPHERE=0
byte BOX=1
byte CYLINDER=2
byte MESH=3

byte type


#### define sphere, box, cylinder ####
# the origin of each shape is considered at the shape's center

# for sphere
# radius := dimensions[0]

# for cylinder
# radius := dimensions[0]
# length := dimensions[1]
# the length is along the Z axis

# for box
# size_x := dimensions[0]
# size_y := dimensions[1]
# size_z := dimensions[2]
float64[] dimensions


#### define mesh ####

# list of triangles; triangle k is defined by tre vertices located
# at indices triangles[3k], triangles[3k+1], triangles[3k+2]
int32[] triangles
geometry_msgs/Point[] vertices

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: brics_3d_msgs/Attribute
# Attribute description for objects in the world model
string key
string value
"""
  __slots__ = ['results']
  _slot_types = ['brics_3d_msgs/SceneObject[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       results
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(GetSceneObjectsResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.results is None:
        self.results = []
    else:
      self.results = []

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
      length = len(self.results)
      buff.write(_struct_I.pack(length))
      for val1 in self.results:
        _x = val1
        buff.write(_struct_2I.pack(_x.id, _x.parentId))
        _v1 = val1.transform
        _v2 = _v1.header
        buff.write(_struct_I.pack(_v2.seq))
        _v3 = _v2.stamp
        _x = _v3
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v2.frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v1.child_frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v4 = _v1.transform
        _v5 = _v4.translation
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = _v4.rotation
        _x = _v6
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v7 = val1.shape
        buff.write(_struct_b.pack(_v7.type))
        length = len(_v7.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *_v7.dimensions))
        length = len(_v7.triangles)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(struct.pack(pattern, *_v7.triangles))
        length = len(_v7.vertices)
        buff.write(_struct_I.pack(length))
        for val3 in _v7.vertices:
          _x = val3
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        length = len(val1.attributes)
        buff.write(_struct_I.pack(length))
        for val2 in val1.attributes:
          _x = val2.key
          length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
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
      (length,) = _struct_I.unpack(str[start:end])
      self.results = []
      for i in range(0, length):
        val1 = brics_3d_msgs.msg.SceneObject()
        _x = val1
        start = end
        end += 8
        (_x.id, _x.parentId,) = _struct_2I.unpack(str[start:end])
        _v8 = val1.transform
        _v9 = _v8.header
        start = end
        end += 4
        (_v9.seq,) = _struct_I.unpack(str[start:end])
        _v10 = _v9.stamp
        _x = _v10
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v9.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v8.child_frame_id = str[start:end]
        _v11 = _v8.transform
        _v12 = _v11.translation
        _x = _v12
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v13 = _v11.rotation
        _x = _v13
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _v14 = val1.shape
        start = end
        end += 1
        (_v14.type,) = _struct_b.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        _v14.dimensions = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        end += struct.calcsize(pattern)
        _v14.triangles = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v14.vertices = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v14.vertices.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.attributes = []
        for i in range(0, length):
          val2 = brics_3d_msgs.msg.Attribute()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          val2.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          val2.value = str[start:end]
          val1.attributes.append(val2)
        self.results.append(val1)
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
      length = len(self.results)
      buff.write(_struct_I.pack(length))
      for val1 in self.results:
        _x = val1
        buff.write(_struct_2I.pack(_x.id, _x.parentId))
        _v15 = val1.transform
        _v16 = _v15.header
        buff.write(_struct_I.pack(_v16.seq))
        _v17 = _v16.stamp
        _x = _v17
        buff.write(_struct_2I.pack(_x.secs, _x.nsecs))
        _x = _v16.frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = _v15.child_frame_id
        length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _v18 = _v15.transform
        _v19 = _v18.translation
        _x = _v19
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v20 = _v18.rotation
        _x = _v20
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        _v21 = val1.shape
        buff.write(_struct_b.pack(_v21.type))
        length = len(_v21.dimensions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(_v21.dimensions.tostring())
        length = len(_v21.triangles)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(_v21.triangles.tostring())
        length = len(_v21.vertices)
        buff.write(_struct_I.pack(length))
        for val3 in _v21.vertices:
          _x = val3
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        length = len(val1.attributes)
        buff.write(_struct_I.pack(length))
        for val2 in val1.attributes:
          _x = val2.key
          length = len(_x)
          buff.write(struct.pack('<I%ss'%length, length, _x))
          _x = val2.value
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
      (length,) = _struct_I.unpack(str[start:end])
      self.results = []
      for i in range(0, length):
        val1 = brics_3d_msgs.msg.SceneObject()
        _x = val1
        start = end
        end += 8
        (_x.id, _x.parentId,) = _struct_2I.unpack(str[start:end])
        _v22 = val1.transform
        _v23 = _v22.header
        start = end
        end += 4
        (_v23.seq,) = _struct_I.unpack(str[start:end])
        _v24 = _v23.stamp
        _x = _v24
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v23.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v22.child_frame_id = str[start:end]
        _v25 = _v22.transform
        _v26 = _v25.translation
        _x = _v26
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v27 = _v25.rotation
        _x = _v27
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        _v28 = val1.shape
        start = end
        end += 1
        (_v28.type,) = _struct_b.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        _v28.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        end += struct.calcsize(pattern)
        _v28.triangles = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v28.vertices = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point()
          _x = val3
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v28.vertices.append(val3)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.attributes = []
        for i in range(0, length):
          val2 = brics_3d_msgs.msg.Attribute()
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          val2.key = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          val2.value = str[start:end]
          val1.attributes.append(val2)
        self.results.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_4d = struct.Struct("<4d")
_struct_b = struct.Struct("<b")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
class GetSceneObjects(roslib.message.ServiceDefinition):
  _type          = 'brics_3d_msgs/GetSceneObjects'
  _md5sum = '6ac508fedc4babc9697964663d676fe7'
  _request_class  = GetSceneObjectsRequest
  _response_class = GetSceneObjectsResponse
