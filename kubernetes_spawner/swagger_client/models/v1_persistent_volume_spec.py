# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1PersistentVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1PersistentVolumeSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'capacity': 'str',
            'gce_persistent_disk': 'V1GCEPersistentDiskVolumeSource',
            'aws_elastic_block_store': 'V1AWSElasticBlockStoreVolumeSource',
            'host_path': 'V1HostPathVolumeSource',
            'glusterfs': 'V1GlusterfsVolumeSource',
            'nfs': 'V1NFSVolumeSource',
            'rbd': 'V1RBDVolumeSource',
            'iscsi': 'V1ISCSIVolumeSource',
            'cinder': 'V1CinderVolumeSource',
            'cephfs': 'V1CephFSVolumeSource',
            'fc': 'V1FCVolumeSource',
            'flocker': 'V1FlockerVolumeSource',
            'flex_volume': 'V1FlexVolumeSource',
            'access_modes': 'list[V1PersistentVolumeAccessMode]',
            'claim_ref': 'V1ObjectReference',
            'persistent_volume_reclaim_policy': 'str'
        }

        self.attribute_map = {
            'capacity': 'capacity',
            'gce_persistent_disk': 'gcePersistentDisk',
            'aws_elastic_block_store': 'awsElasticBlockStore',
            'host_path': 'hostPath',
            'glusterfs': 'glusterfs',
            'nfs': 'nfs',
            'rbd': 'rbd',
            'iscsi': 'iscsi',
            'cinder': 'cinder',
            'cephfs': 'cephfs',
            'fc': 'fc',
            'flocker': 'flocker',
            'flex_volume': 'flexVolume',
            'access_modes': 'accessModes',
            'claim_ref': 'claimRef',
            'persistent_volume_reclaim_policy': 'persistentVolumeReclaimPolicy'
        }

        self._capacity = None
        self._gce_persistent_disk = None
        self._aws_elastic_block_store = None
        self._host_path = None
        self._glusterfs = None
        self._nfs = None
        self._rbd = None
        self._iscsi = None
        self._cinder = None
        self._cephfs = None
        self._fc = None
        self._flocker = None
        self._flex_volume = None
        self._access_modes = None
        self._claim_ref = None
        self._persistent_volume_reclaim_policy = None

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity

        :return: The capacity of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#capacity

        :param capacity: The capacity of this V1PersistentVolumeSpec.
        :type: str
        """
        self._capacity = capacity

    @property
    def gce_persistent_disk(self):
        """
        Gets the gce_persistent_disk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :return: The gce_persistent_disk of this V1PersistentVolumeSpec.
        :rtype: V1GCEPersistentDiskVolumeSource
        """
        return self._gce_persistent_disk

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk):
        """
        Sets the gce_persistent_disk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :param gce_persistent_disk: The gce_persistent_disk of this V1PersistentVolumeSpec.
        :type: V1GCEPersistentDiskVolumeSource
        """
        self._gce_persistent_disk = gce_persistent_disk

    @property
    def aws_elastic_block_store(self):
        """
        Gets the aws_elastic_block_store of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#awselasticblockstore

        :return: The aws_elastic_block_store of this V1PersistentVolumeSpec.
        :rtype: V1AWSElasticBlockStoreVolumeSource
        """
        return self._aws_elastic_block_store

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store):
        """
        Sets the aws_elastic_block_store of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#awselasticblockstore

        :param aws_elastic_block_store: The aws_elastic_block_store of this V1PersistentVolumeSpec.
        :type: V1AWSElasticBlockStoreVolumeSource
        """
        self._aws_elastic_block_store = aws_elastic_block_store

    @property
    def host_path(self):
        """
        Gets the host_path of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#hostpath

        :return: The host_path of this V1PersistentVolumeSpec.
        :rtype: V1HostPathVolumeSource
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """
        Sets the host_path of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#hostpath

        :param host_path: The host_path of this V1PersistentVolumeSpec.
        :type: V1HostPathVolumeSource
        """
        self._host_path = host_path

    @property
    def glusterfs(self):
        """
        Gets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/glusterfs/README.md

        :return: The glusterfs of this V1PersistentVolumeSpec.
        :rtype: V1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """
        Sets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/glusterfs/README.md

        :param glusterfs: The glusterfs of this V1PersistentVolumeSpec.
        :type: V1GlusterfsVolumeSource
        """
        self._glusterfs = glusterfs

    @property
    def nfs(self):
        """
        Gets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#nfs

        :return: The nfs of this V1PersistentVolumeSpec.
        :rtype: V1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#nfs

        :param nfs: The nfs of this V1PersistentVolumeSpec.
        :type: V1NFSVolumeSource
        """
        self._nfs = nfs

    @property
    def rbd(self):
        """
        Gets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/rbd/README.md

        :return: The rbd of this V1PersistentVolumeSpec.
        :rtype: V1RBDVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """
        Sets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/rbd/README.md

        :param rbd: The rbd of this V1PersistentVolumeSpec.
        :type: V1RBDVolumeSource
        """
        self._rbd = rbd

    @property
    def iscsi(self):
        """
        Gets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :return: The iscsi of this V1PersistentVolumeSpec.
        :rtype: V1ISCSIVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """
        Sets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :param iscsi: The iscsi of this V1PersistentVolumeSpec.
        :type: V1ISCSIVolumeSource
        """
        self._iscsi = iscsi

    @property
    def cinder(self):
        """
        Gets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The cinder of this V1PersistentVolumeSpec.
        :rtype: V1CinderVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """
        Sets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param cinder: The cinder of this V1PersistentVolumeSpec.
        :type: V1CinderVolumeSource
        """
        self._cinder = cinder

    @property
    def cephfs(self):
        """
        Gets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :return: The cephfs of this V1PersistentVolumeSpec.
        :rtype: V1CephFSVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """
        Sets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :param cephfs: The cephfs of this V1PersistentVolumeSpec.
        :type: V1CephFSVolumeSource
        """
        self._cephfs = cephfs

    @property
    def fc(self):
        """
        Gets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :return: The fc of this V1PersistentVolumeSpec.
        :rtype: V1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """
        Sets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :param fc: The fc of this V1PersistentVolumeSpec.
        :type: V1FCVolumeSource
        """
        self._fc = fc

    @property
    def flocker(self):
        """
        Gets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :return: The flocker of this V1PersistentVolumeSpec.
        :rtype: V1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """
        Sets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :param flocker: The flocker of this V1PersistentVolumeSpec.
        :type: V1FlockerVolumeSource
        """
        self._flocker = flocker

    @property
    def flex_volume(self):
        """
        Gets the flex_volume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using a exec based plugin. This is an alpha feature and may change in future.

        :return: The flex_volume of this V1PersistentVolumeSpec.
        :rtype: V1FlexVolumeSource
        """
        return self._flex_volume

    @flex_volume.setter
    def flex_volume(self, flex_volume):
        """
        Sets the flex_volume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using a exec based plugin. This is an alpha feature and may change in future.

        :param flex_volume: The flex_volume of this V1PersistentVolumeSpec.
        :type: V1FlexVolumeSource
        """
        self._flex_volume = flex_volume

    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes

        :return: The access_modes of this V1PersistentVolumeSpec.
        :rtype: list[V1PersistentVolumeAccessMode]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#access-modes

        :param access_modes: The access_modes of this V1PersistentVolumeSpec.
        :type: list[V1PersistentVolumeAccessMode]
        """
        self._access_modes = access_modes

    @property
    def claim_ref(self):
        """
        Gets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#binding

        :return: The claim_ref of this V1PersistentVolumeSpec.
        :rtype: V1ObjectReference
        """
        return self._claim_ref

    @claim_ref.setter
    def claim_ref(self, claim_ref):
        """
        Sets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#binding

        :param claim_ref: The claim_ref of this V1PersistentVolumeSpec.
        :type: V1ObjectReference
        """
        self._claim_ref = claim_ref

    @property
    def persistent_volume_reclaim_policy(self):
        """
        Gets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recyling must be supported by the volume plugin underlying this persistent volume. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#recycling-policy

        :return: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._persistent_volume_reclaim_policy

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, persistent_volume_reclaim_policy):
        """
        Sets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recyling must be supported by the volume plugin underlying this persistent volume. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#recycling-policy

        :param persistent_volume_reclaim_policy: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :type: str
        """
        self._persistent_volume_reclaim_policy = persistent_volume_reclaim_policy

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

