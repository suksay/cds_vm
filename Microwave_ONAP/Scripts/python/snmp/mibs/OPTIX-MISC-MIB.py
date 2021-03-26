#
# PySNMP MIB module OPTIX-MISC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/OPTIX-MISC-MIB.mib
# Produced by pysmi-0.3.4 at Tue Jun 16 14:22:51 2020
# On host DESKTOP-LULODOL platform Linux version 4.19.84-microsoft-standard by user root
# Using Python version 3.7.3 (default, Dec 20 2019, 18:57:59) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
optixProvisionEqpt, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixProvisionEqpt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Bits, Integer32, iso, Counter32, Gauge32, TimeTicks, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "Integer32", "iso", "Counter32", "Gauge32", "TimeTicks", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
optixMisc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39))
optixMisc.setRevisions(('2012-04-24 00:00', '2012-04-24 00:00',))
if mibBuilder.loadTexts: optixMisc.setLastUpdated('201204240000Z')
if mibBuilder.loadTexts: optixMisc.setOrganization('Huawei Technologies co.,Ltd.')
optixMiscGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1))
optixFanSpeed = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 1, 2, 3, 5, 6, 7, 9))).clone(namedValues=NamedValues(("stop", 4), ("low", 1), ("mid", 2), ("high", 3), ("autolow", 5), ("automid", 6), ("autohigh", 7), ("auto", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixFanSpeed.setStatus('current')
optixFanMinDispersion = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixFanMinDispersion.setStatus('current')
optixEnvironmentTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3), )
if mibBuilder.loadTexts: optixEnvironmentTable.setStatus('current')
optixEnvironmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"))
if mibBuilder.loadTexts: optixEnvironmentEntry.setStatus('current')
optixEnvironmentBdId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: optixEnvironmentBdId.setStatus('current')
optixRelayControlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("pmuauto", 0), ("pmumanual", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayControlMode.setStatus('current')
optixRelayNormalAlmState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("open", 1), ("close", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayNormalAlmState.setStatus('current')
optixRelaySeriousAlmState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("open", 1), ("close", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelaySeriousAlmState.setStatus('current')
optixRelayTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4), )
if mibBuilder.loadTexts: optixRelayTable.setStatus('current')
optixRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"), (0, "OPTIX-MISC-MIB", "optixRelayId"))
if mibBuilder.loadTexts: optixRelayEntry.setStatus('current')
optixRelayId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: optixRelayId.setStatus('current')
optixRelayUseState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayUseState.setStatus('current')
optixRelayAlmSwitchState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("open", 1), ("close", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayAlmSwitchState.setStatus('current')
optixRelayAlmLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("critical", 0), ("major", 1), ("minor", 2), ("ignore", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayAlmLevel.setStatus('current')
optixRelayOutState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("close", 0), ("open", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayOutState.setStatus('current')
optixAlmOutputTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5), )
if mibBuilder.loadTexts: optixAlmOutputTable.setStatus('current')
optixAlmOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"), (0, "OPTIX-MISC-MIB", "optixAlmOutputLevel"))
if mibBuilder.loadTexts: optixAlmOutputEntry.setStatus('current')
optixAlmOutputLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("ignore", 4))))
if mibBuilder.loadTexts: optixAlmOutputLevel.setStatus('current')
optixAlmOutputNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixAlmOutputNum.setStatus('current')
optixRelayNameTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6), )
if mibBuilder.loadTexts: optixRelayNameTable.setStatus('current')
optixRelayNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixEnvironmentBdId"), (0, "OPTIX-MISC-MIB", "optixRelayId"), (0, "OPTIX-MISC-MIB", "optixRelayType"))
if mibBuilder.loadTexts: optixRelayNameEntry.setStatus('current')
optixRelayType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("all", 0), ("input", 1), ("ext", 2))))
if mibBuilder.loadTexts: optixRelayType.setStatus('current')
optixRelayName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 21))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixRelayName.setStatus('current')
optixOamPortMngTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7), )
if mibBuilder.loadTexts: optixOamPortMngTable.setStatus('current')
optixOamPortMngEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixOamBdId"), (0, "OPTIX-MISC-MIB", "optixOamSubBdId"), (0, "OPTIX-MISC-MIB", "optixOamPortId"))
if mibBuilder.loadTexts: optixOamPortMngEntry.setStatus('current')
optixOamBdId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: optixOamBdId.setStatus('current')
optixOamSubBdId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 2), Unsigned32())
if mibBuilder.loadTexts: optixOamSubBdId.setStatus('current')
optixOamPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 3), Unsigned32())
if mibBuilder.loadTexts: optixOamPortId.setStatus('current')
optixOamPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("all", 0), ("com", 1), ("eth", 2), ("oam", 3), ("fF", 4), ("ext", 5), ("usb", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixOamPortType.setStatus('current')
optixOamPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("open", 1), ("close", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixOamPortState.setStatus('current')
optixCommuMngTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8), )
if mibBuilder.loadTexts: optixCommuMngTable.setStatus('current')
optixCommuMngEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixCommuBdId"), (0, "OPTIX-MISC-MIB", "optixCommuSubBdId"), (0, "OPTIX-MISC-MIB", "optixCommuPortId"))
if mibBuilder.loadTexts: optixCommuMngEntry.setStatus('current')
optixCommuBdId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 1), Unsigned32())
if mibBuilder.loadTexts: optixCommuBdId.setStatus('current')
optixCommuSubBdId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 2), Unsigned32())
if mibBuilder.loadTexts: optixCommuSubBdId.setStatus('current')
optixCommuPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 3), Unsigned32())
if mibBuilder.loadTexts: optixCommuPortId.setStatus('current')
optixEthPortAdaptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("adapt", 1), ("fixed", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixEthPortAdaptMode.setStatus('current')
optixEthPortAdaptSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 254, 255))).clone(namedValues=NamedValues(("snmp100m", 1), ("snmp10m", 0), ("commufail", 254), ("inautonego", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixEthPortAdaptSpeed.setStatus('current')
optixEthPortAdaptDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 254, 255))).clone(namedValues=NamedValues(("full", 1), ("half", 0), ("commufail", 254), ("inautonego", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixEthPortAdaptDuplex.setStatus('current')
optixCommuRealMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("fixed", 0), ("adapt", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixCommuRealMode.setStatus('current')
optixCommuRealSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 254, 255))).clone(namedValues=NamedValues(("snmp10m", 0), ("snmp100m", 1), ("commufail", 254), ("inautonego", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixCommuRealSpeed.setStatus('current')
optixCommuRealDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 254, 255))).clone(namedValues=NamedValues(("half", 0), ("full", 1), ("commufail", 254), ("inautonego", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: optixCommuRealDuplex.setStatus('current')
optixPowerMonstateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9), )
if mibBuilder.loadTexts: optixPowerMonstateTable.setStatus('current')
optixPowerMonstateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1), ).setIndexNames((0, "OPTIX-MISC-MIB", "optixPowerMonstateSlotId"), (0, "OPTIX-MISC-MIB", "optixPowerMonstatePort"))
if mibBuilder.loadTexts: optixPowerMonstateEntry.setStatus('current')
optixPowerMonstateSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536)))
if mibBuilder.loadTexts: optixPowerMonstateSlotId.setStatus('current')
optixPowerMonstatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: optixPowerMonstatePort.setStatus('current')
optixPowerMonstateState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixPowerMonstateState.setStatus('current')
optixMiscextGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 2))
optixFanSpeedext = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30, 39, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: optixFanSpeedext.setStatus('current')
mibBuilder.exportSymbols("OPTIX-MISC-MIB", optixRelayEntry=optixRelayEntry, optixOamSubBdId=optixOamSubBdId, optixRelayTable=optixRelayTable, optixPowerMonstatePort=optixPowerMonstatePort, optixEthPortAdaptDuplex=optixEthPortAdaptDuplex, optixRelayName=optixRelayName, optixPowerMonstateTable=optixPowerMonstateTable, optixOamPortId=optixOamPortId, optixEnvironmentEntry=optixEnvironmentEntry, optixOamPortState=optixOamPortState, optixOamPortType=optixOamPortType, optixAlmOutputLevel=optixAlmOutputLevel, optixMiscextGroup=optixMiscextGroup, optixEnvironmentBdId=optixEnvironmentBdId, optixRelayNormalAlmState=optixRelayNormalAlmState, optixPowerMonstateEntry=optixPowerMonstateEntry, optixRelaySeriousAlmState=optixRelaySeriousAlmState, optixMisc=optixMisc, optixEthPortAdaptSpeed=optixEthPortAdaptSpeed, optixCommuPortId=optixCommuPortId, optixRelayAlmSwitchState=optixRelayAlmSwitchState, optixRelayOutState=optixRelayOutState, optixCommuMngTable=optixCommuMngTable, optixFanSpeed=optixFanSpeed, optixMiscGroup=optixMiscGroup, optixEthPortAdaptMode=optixEthPortAdaptMode, optixOamPortMngEntry=optixOamPortMngEntry, optixRelayNameEntry=optixRelayNameEntry, optixAlmOutputTable=optixAlmOutputTable, optixRelayNameTable=optixRelayNameTable, PYSNMP_MODULE_ID=optixMisc, optixCommuRealMode=optixCommuRealMode, optixFanSpeedext=optixFanSpeedext, optixCommuMngEntry=optixCommuMngEntry, optixEnvironmentTable=optixEnvironmentTable, optixAlmOutputNum=optixAlmOutputNum, optixRelayType=optixRelayType, optixAlmOutputEntry=optixAlmOutputEntry, optixPowerMonstateState=optixPowerMonstateState, optixRelayId=optixRelayId, optixRelayUseState=optixRelayUseState, optixRelayAlmLevel=optixRelayAlmLevel, optixCommuSubBdId=optixCommuSubBdId, optixCommuRealDuplex=optixCommuRealDuplex, optixPowerMonstateSlotId=optixPowerMonstateSlotId, optixOamBdId=optixOamBdId, optixCommuBdId=optixCommuBdId, optixRelayControlMode=optixRelayControlMode, optixFanMinDispersion=optixFanMinDispersion, optixCommuRealSpeed=optixCommuRealSpeed, optixOamPortMngTable=optixOamPortMngTable)