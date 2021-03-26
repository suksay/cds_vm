#
# PySNMP MIB module OPTIX-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/OPTIX-OID-MIB.mib
# Produced by pysmi-0.3.4 at Thu Jun 11 11:56:19 2020
# On host DESKTOP-LULODOL platform Linux version 4.19.84-microsoft-standard by user root
# Using Python version 3.7.3 (default, Dec 20 2019, 18:57:59) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Integer32, Unsigned32, Counter64, Bits, Gauge32, MibIdentifier, enterprises, ModuleIdentity, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Integer32", "Unsigned32", "Counter64", "Bits", "Gauge32", "MibIdentifier", "enterprises", "ModuleIdentity", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
transmission = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25))
optixCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3))
optixCommonSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 1))
optixCommonSdh = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 10))
optixCommonSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20))
optixNGWDM = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 30))
optixCommonGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 40))
optixNGWDMGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 50))
optixPtnGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 60))
rtn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 70))
optixProvision = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4))
optixProvisionSdh = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 10))
optixProvisionSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 20))
optixProvisionEqpt = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 30))
optixProvisionRtn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 40))
optixProvisionPtn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 25, 4, 50))
mibBuilder.exportSymbols("OPTIX-OID-MIB", optixCommonSnmp=optixCommonSnmp, optixNGWDM=optixNGWDM, products=products, optixCommon=optixCommon, optixProvisionSdh=optixProvisionSdh, optixNGWDMGlobal=optixNGWDMGlobal, huawei=huawei, optixCommonSdh=optixCommonSdh, optixProvisionRtn=optixProvisionRtn, optixPtnGlobal=optixPtnGlobal, optixProvision=optixProvision, optixCommonSonet=optixCommonSonet, optixCommonGlobal=optixCommonGlobal, optixProvisionSonet=optixProvisionSonet, optixProvisionPtn=optixProvisionPtn, rtn=rtn, optixProvisionEqpt=optixProvisionEqpt, transmission=transmission)