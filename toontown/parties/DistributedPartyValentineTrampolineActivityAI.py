from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI


class DistributedPartyValentineTrampolineActivityAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'DistributedPartyValentineTrampolineActivityAI')
