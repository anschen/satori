import untangle
import struct


# grab the latest fingerprint files:
# wget chatteronthewire.org/download/updates/satori/fingerprints/dhcp.xml -O dhcp.xml
#
# looking for new fingerprints
# python3 satori.py -r dhcp.pcap -m dhcp > output.txt
# cat output.txt | awk -F';' '{print $3, $4, $5, $6, $7}' | sort -u > output2.txt
#


def BuildDHCPFingerprintFiles():
  # converting from the xml format to a more flat format that will hopefully be faster than walking the entire xml every FP lookup
  # this got much larger than I thought it would!
  DiscoverOptionsExactList = {}
  DiscoverOptionsPartialList = {}
  RequestOptionsExactList = {}
  RequestOptionsPartialList = {}
  ReleaseOptionsExactList = {}
  ReleaseOptionsPartialList = {}
  ACKOptionsExactList = {}
  ACKOptionsPartialList = {}
  AnyOptionsExactList = {}
  AnyOptionsPartialList = {}
  InformOptionsExactList = {}
  InformOptionsPartialList = {}
  DiscoverOption55ExactList = {}
  DiscoverOption55PartialList = {}
  RequestOption55ExactList = {}
  RequestOption55PartialList = {}
  ReleaseOption55ExactList = {}
  ReleaseOption55PartialList = {}
  ACKOption55ExactList = {}
  ACKOption55PartialList = {}
  AnyOption55ExactList = {}
  AnyOption55PartialList = {}
  InformOption55ExactList = {}
  InformOption55PartialList = {}
  DiscoverVendorCodeExactList = {}
  DiscoverVendorCodePartialList = {}
  RequestVendorCodeExactList = {}
  RequestVendorCodePartialList = {}
  ReleaseVendorCodeExactList = {}
  ReleaseVendorCodePartialList = {}
  ACKVendorCodeExactList = {}
  ACKVendorCodePartialList = {}
  AnyVendorCodeExactList = {}
  AnyVendorCodePartialList = {}
  InformVendorCodeExactList = {}
  InformVendorCodePartialList = {}
  DiscoverTTLExactList = {}
  DiscoverTTLPartialList = {}
  RequestTTLExactList = {}
  RequestTTLPartialList = {}
  ReleaseTTLExactList = {}
  ACKTTLExactList = {}
  AnyTTLExactList = {}
  InformTTLExactList = {}
  ACKTTLPartialList = {}
  AnyTTLPartialList = {}
  InformTTLPartialList = {}

  NAKOptionsPartialList = {}
  NAKOptionsExactList = {}
  NAKOption55PartialList = {}
  NAKOption55ExactList = {}
  NAKVendorCodePartialList = {}
  NAKVendorCodeExactList = {}
  NAKTTLPartialList = {}
  NAKTTLExactList = {}

  OfferOptionsPartialList = {}
  OfferOptionsExactList = {}
  OfferOption55PartialList = {}
  OfferOption55ExactList = {}
  OfferVendorCodePartialList = {}
  OfferVendorCodeExactList = {}
  OfferTTLPartialList = {}
  OfferTTLExactList = {}

  DeclineOptionsPartialList = {}
  DeclineOptionsExactList = {}
  DeclineOption55PartialList = {}
  DeclineOption55ExactList = {}
  DeclineVendorCodePartialList = {}
  DeclineVendorCodeExactList = {}
  DeclineTTLPartialList = {}
  DeclineTTLExactList = {}

  #need to decide how to deal with ; in dhcpvendorcode


  obj = untangle.parse('dhcp.xml')
  fingerprintsCount = len(obj.DHCP.fingerprints)
  for x in range(0,fingerprintsCount):
    os = obj.DHCP.fingerprints.fingerprint[x]['name']
    testsCount = len(obj.DHCP.fingerprints.fingerprint[x].dhcp_tests)
    test = {}
    for y in range(0,testsCount):
      test = obj.DHCP.fingerprints.fingerprint[x].dhcp_tests.test[y]
      if test is None:  #if testsCount = 1, then untangle doesn't allow us to iterate through it
        test = obj.DHCP.fingerprints.fingerprint[x].dhcp_tests.test
      matchtype = test['matchtype']
      dhcptype = test['dhcptype']
      weight = test['weight']
      #some won't exist each time, is that going to be a problem??
      dhcpoption55 = test['dhcpoption55']
      dhcpvendorcode = test['dhcpvendorcode']
      dhcpoptions = test['dhcpoptions']
      ipttl = test['ipttl']

      if matchtype == 'exact':
        if dhcptype == 'Discover' and dhcpoptions != None:
          if dhcpoptions in DiscoverOptionsExactList:
            oldValue = DiscoverOptionsExactList.get(dhcpoptions)
            DiscoverOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Request' and dhcpoptions != None:
          if dhcpoptions in RequestOptionsExactList:
            oldValue = RequestOptionsExactList.get(dhcpoptions)
            RequestOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            RequestOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Release' and dhcpoptions != None:
          if dhcpoptions in ReleaseOptionsExactList:
            oldValue = ReleaseOptionsExactList.get(dhcpoptions)
            ReleaseOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'ACK' and dhcpoptions != None:
          if dhcpoptions in ACKOptionsExactList:
            oldValue = ACKOptionsExactList.get(dhcpoptions)
            ACKOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            ACKOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Any' and dhcpoptions != None:
          if dhcpoptions in AnyOptionsExactList:
            oldValue = AnyOptionsExactList.get(dhcpoptions)
            AnyOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            AnyOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Inform' and dhcpoptions != None:
          if dhcpoptions in InformOptionsExactList:
            oldValue = InformOptionsExactList.get(dhcpoptions)
            InformOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            InformOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'NAK' and dhcpoptions != None:
          if dhcpoptions in NAKOptionsExactList:
            oldValue = NAKOptionsExactList.get(dhcpoptions)
            NAKOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            NAKOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Offer' and dhcpoptions != None:
          if dhcpoptions in OfferOptionsExactList:
            oldValue = OfferOptionsExactList.get(dhcpoptions)
            OfferOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            OfferOptionsExactList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Decline' and dhcpoptions != None:
          if dhcpoptions in DeclineOptionsExactList:
            oldValue = DeclineOptionsExactList.get(dhcpoptions)
            DeclineOptionsExactList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            DeclineOptionsExactList[dhcpoptions] = os + ':' + weight

        elif dhcptype == 'Discover' and dhcpoption55 != None:
          if dhcpoption55 in DiscoverOption55ExactList:
            oldValue = DiscoverOption55ExactList.get(dhcpoption55)
            DiscoverOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Request' and dhcpoption55 != None:
          if dhcpoption55 in RequestOption55ExactList:
            oldValue = RequestOption55ExactList.get(dhcpoption55)
            RequestOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            RequestOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Release' and dhcpoption55 != None:
          if dhcpoption55 in ReleaseOption55ExactList:
            oldValue = ReleaseOption55ExactList.get(dhcpoption55)
            ReleaseOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'ACK' and dhcpoption55 != None:
          if dhcpoption55 in ACKOption55ExactList:
            oldValue = ACKOption55ExactList.get(dhcpoption55)
            ACKOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            ACKOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Any' and dhcpoption55 != None:
          if dhcpoption55 in AnyOption55ExactList:
            oldValue = AnyOption55ExactList.get(dhcpoption55)
            AnyOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            AnyOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Inform' and dhcpoption55 != None:
          if dhcpoption55 in InformOption55ExactList:
            oldValue = InformOption55ExactList.get(dhcpoption55)
            InformOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            InformOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'NAK' and dhcpoption55 != None:
          if dhcpoption55 in NAKOption55ExactList:
            oldValue = NAKOption55ExactList.get(dhcpoption55)
            NAKOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            NAKOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Offer' and dhcpoption55 != None:
          if dhcpoption55 in OfferOption55ExactList:
            oldValue = OfferOption55ExactList.get(dhcpoption55)
            OfferOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            OfferOption55ExactList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Decline' and dhcpoption55 != None:
          if dhcpoption55 in DeclineOption55ExactList:
            oldValue = DeclineOption55ExactList.get(dhcpoption55)
            DeclineOption55ExactList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            DeclineOption55ExactList[dhcpoption55] = os + ':' + weight

        elif dhcptype == 'Discover' and dhcpvendorcode != None:
          if dhcpvendorcode in DiscoverVendorCodeExactList:
            oldValue = DiscoverVendorCodeExactList.get(dhcpvendorcode)
            DiscoverVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Request' and dhcpvendorcode != None:
          if dhcpvendorcode in RequestVendorCodeExactList:
            oldValue = RequestVendorCodeExactList.get(dhcpvendorcode)
            RequestVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            RequestVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Release' and dhcpvendorcode != None:
          if dhcpvendorcode in ReleaseVendorCodeExactList:
            oldValue = ReleaseVendorCodeExactList.get(dhcpvendorcode)
            ReleaseVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'ACK' and dhcpvendorcode != None:
          if dhcpvendorcode in ACKVendorCodeExactList:
            oldValue = ACKVendorCodeExactList.get(dhcpvendorcode)
            ACKVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            ACKVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Any' and dhcpvendorcode != None:
          if dhcpvendorcode in AnyVendorCodeExactList:
            oldValue = AnyVendorCodeExactList.get(dhcpvendorcode)
            AnyVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            AnyVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Inform' and dhcpvendorcode != None:
          if dhcpvendorcode in InformVendorCodeExactList:
            oldValue = InformVendorCodeExactList.get(dhcpvendorcode)
            InformVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            InformVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'NAK' and dhcpvendorcode != None:
          if dhcpvendorcode in NAKVendorCodeExactList:
            oldValue = NAKVendorCodeExactList.get(dhcpvendorcode)
            NAKVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            NAKVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Offer' and dhcpvendorcode != None:
          if dhcpvendorcode in OfferVendorCodeExactList:
            oldValue = OfferVendorCodeExactList.get(dhcpvendorcode)
            OfferVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            OfferVendorCodeExactList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Decline' and dhcpvendorcode != None:
          if dhcpvendorcode in DeclineVendorCodeExactList:
            oldValue = DeclineVendorCodeExactList.get(dhcpvendorcode)
            DeclineVendorCodeExactList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            DeclineVendorCodeExactList[dhcpvendorcode] = os + ':' + weight

        elif dhcptype == 'Discover' and ipttl != None:
          if ipttl in DiscoverTTLExactList:
            oldValue = DiscoverTTLExactList.get(ipttl)
            DiscoverTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'Request' and ipttl != None:
          if ipttl in RequestTTLExactList:
            oldValue = RequestTTLExactList.get(ipttl)
            RequestTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            RequestTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'Release' and ipttl != None:
          if ipttl in ReleaseTTLExactList:
            oldValue = ReleaseTTLExactList.get(ipttl)
            ReleaseTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'ACK' and ipttl != None:
          if ipttl in ACKTTLExactList:
            oldValue = ACKTTLExactList.get(ipttl)
            ACKTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            ACKTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'Any' and ipttl != None:
          if ipttl in AnyTTLExactList:
            oldValue = AnyTTLExactList.get(ipttl)
            AnyTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            AnyTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'Inform' and ipttl != None:
          if ipttl in InformTTLExactList:
            oldValue = InformTTLExactList.get(ipttl)
            InformTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            InformTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'NAK' and ipttl != None:
          if ipttl in NAKTTLExactList:
            oldValue = NAKTTLExactList.get(ipttl)
            NAKTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            NAKTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'Offer' and ipttl != None:
          if ipttl in OfferTTLExactList:
            oldValue = OfferTTLExactList.get(ipttl)
            OfferTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            OfferTTLExactList[ipttl] = os + ':' + weight
        elif dhcptype == 'Decline' and ipttl != None:
          if ipttl in DeclineTTLExactList:
            oldValue = DeclineTTLExactList.get(ipttl)
            DeclineTTLExactList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            DeclineTTLExactList[ipttl] = os + ':' + weight


      elif matchtype == 'partial':
        if dhcptype == 'Discover' and dhcpoptions != None:
          if dhcpoptions in DiscoverOptionsPartialList:
            oldValue = DiscoverOptionsPartialList.get(dhcpoptions)
            DiscoverOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Request' and dhcpoptions != None:
          if dhcpoptions in RequestOptionsPartialList:
            oldValue = RequestOptionsPartialList.get(dhcpoptions)
            RequestOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            RequestOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Release' and dhcpoptions != None:
          if dhcpoptions in ReleaseOptionsPartialList:
            oldValue = ReleaseOptionsPartialList.get(dhcpoptions)
            ReleaseOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'ACK' and dhcpoptions != None:
          if dhcpoptions in ACKOptionsPartialList:
            oldValue = ACKOptionsPartialList.get(dhcpoptions)
            ACKOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            ACKOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Any' and dhcpoptions != None:
          if dhcpoptions in AnyOptionsPartialList:
            oldValue = AnyOptionsPartialList.get(dhcpoptions)
            AnyOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            AnyOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Inform' and dhcpoptions != None:
          if dhcpoptions in InformOptionsPartialList:
            oldValue = InformOptionsPartialList.get(dhcpoptions)
            InformOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            InformOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'NAK' and dhcpoptions != None:
          if dhcpoptions in NAKOptionsPartialList:
            oldValue = NAKOptionsPartialList.get(dhcpoptions)
            NAKOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            NAKOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Offer' and dhcpoptions != None:
          if dhcpoptions in OfferOptionsPartialList:
            oldValue = OfferOptionsPartialList.get(dhcpoptions)
            OfferOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            OfferOptionsPartialList[dhcpoptions] = os + ':' + weight
        elif dhcptype == 'Decline' and dhcpoptions != None:
          if dhcpoptions in DeclineOptionsPartialList:
            oldValue = DeclineOptionsPartialList.get(dhcpoptions)
            DeclineOptionsPartialList[dhcpoptions] = oldValue + '|' + os + ':' + weight
          else:
            DeclineOptionsPartialList[dhcpoptions] = os + ':' + weight

        elif dhcptype == 'Discover' and dhcpoption55 != None:
          if dhcpoption55 in DiscoverOption55PartialList:
            oldValue = DiscoverOption55PartialList.get(dhcpoption55)
            DiscoverOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Request' and dhcpoption55 != None:
          if dhcpoption55 in RequestOption55PartialList:
            oldValue = RequestOption55PartialList.get(dhcpoption55)
            RequestOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            RequestOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Release' and dhcpoption55 != None:
          if dhcpoption55 in ReleaseOption55PartialList:
            oldValue = ReleaseOption55PartialList.get(dhcpoption55)
            ReleaseOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'ACK' and dhcpoption55 != None:
          if dhcpoption55 in ACKOption55PartialList:
            oldValue = ACKOption55PartialList.get(dhcpoption55)
            ACKOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            ACKOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Any' and dhcpoption55 != None:
          if dhcpoption55 in AnyOption55PartialList:
            oldValue = AnyOption55PartialList.get(dhcpoption55)
            AnyOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            AnyOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Inform' and dhcpoption55 != None:
          if dhcpoption55 in InformOption55PartialList:
            oldValue = InformOption55PartialList.get(dhcpoption55)
            InformOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            InformOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'NAK' and dhcpoption55 != None:
          if dhcpoption55 in NAKOption55PartialList:
            oldValue = NAKOption55PartialList.get(dhcpoption55)
            NAKOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            NAKOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Offer' and dhcpoption55 != None:
          if dhcpoption55 in OfferOption55PartialList:
            oldValue = OfferOption55PartialList.get(dhcpoption55)
            OfferOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            OfferOption55PartialList[dhcpoption55] = os + ':' + weight
        elif dhcptype == 'Decline' and dhcpoption55 != None:
          if dhcpoption55 in DeclineOption55PartialList:
            oldValue = DeclineOption55PartialList.get(dhcpoption55)
            DeclineOption55PartialList[dhcpoption55] = oldValue + '|' + os + ':' + weight
          else:
            DeclineOption55PartialList[dhcpoption55] = os + ':' + weight

        elif dhcptype == 'Discover' and dhcpvendorcode != None:
          if dhcpvendorcode in DiscoverVendorCodePartialList:
            oldValue = DiscoverVendorCodePartialList.get(dhcpvendorcode)
            DiscoverVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Request' and dhcpvendorcode != None:
          if dhcpvendorcode in RequestVendorCodePartialList:
            oldValue = RequestVendorCodePartialList.get(dhcpvendorcode)
            RequestVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            RequestVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Release' and dhcpvendorcode != None:
          if dhcpvendorcode in ReleaseVendorCodePartialList:
            oldValue = ReleaseVendorCodePartialList.get(dhcpvendorcode)
            ReleaseVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'ACK' and dhcpvendorcode != None:
          if dhcpvendorcode in ACKVendorCodePartialList:
            oldValue = ACKVendorCodePartialList.get(dhcpvendorcode)
            ACKVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            ACKVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Any' and dhcpvendorcode != None:
          if dhcpvendorcode in AnyVendorCodePartialList:
            oldValue = AnyVendorCodePartialList.get(dhcpvendorcode)
            AnyVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            AnyVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Inform' and dhcpvendorcode != None:
          if dhcpvendorcode in InformVendorCodePartialList:
            oldValue = InformVendorCodePartialList.get(dhcpvendorcode)
            InformVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            InformVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'NAK' and dhcpvendorcode != None:
          if dhcpvendorcode in NAKVendorCodePartialList:
            oldValue = NAKVendorCodePartialList.get(dhcpvendorcode)
            NAKVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            NAKVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Offer' and dhcpvendorcode != None:
          if dhcpvendorcode in OfferVendorCodePartialList:
            oldValue = OfferVendorCodePartialList.get(dhcpvendorcode)
            OfferVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            OfferVendorCodePartialList[dhcpvendorcode] = os + ':' + weight
        elif dhcptype == 'Decline' and dhcpvendorcode != None:
          if dhcpvendorcode in DeclineVendorCodePartialList:
            oldValue = DeclineVendorCodePartialList.get(dhcpvendorcode)
            DeclineVendorCodePartialList[dhcpvendorcode] = oldValue + '|' + os + ':' + weight
          else:
            DeclineVendorCodePartialList[dhcpvendorcode] = os + ':' + weight

        elif dhcptype == 'Discover' and ipttl != None:
          if ipttl in DiscoverTTLPartialList:
            oldValue = DiscoverTTLPartialList.get(ipttl)
            DiscoverTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            DiscoverTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'Request' and ipttl != None:
          if ipttl in RequestTTLPartialList:
            oldValue = RequestTTLPartialList.get(ipttl)
            RequestTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            RequestTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'Release' and ipttl != None:
          if ipttl in ReleaseTTLPartialList:
            oldValue = ReleaseTTLPartialList.get(ipttl)
            ReleaseTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            ReleaseTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'ACK' and ipttl != None:
          if ipttl in ACKTTLPartialList:
            oldValue = ACKTTLPartialList.get(ipttl)
            ACKTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            ACKTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'Any' and ipttl != None:
          if ipttl in AnyTTLPartialList:
            oldValue = AnyTTLPartialList.get(ipttl)
            AnyTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            AnyTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'Inform' and ipttl != None:
          if ipttl in InformTTLPartialList:
            oldValue = InformTTLPartialList.get(ipttl)
            InformTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            InformTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'NAK' and ipttl != None:
          if ipttl in NAKTTLPartialList:
            oldValue = NAKTTLPartialList.get(ipttl)
            NAKTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            NAKTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'Offer' and ipttl != None:
          if ipttl in OfferTTLPartialList:
            oldValue = OfferTTLPartialList.get(ipttl)
            OfferTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            OfferTTLPartialList[ipttl] = os + ':' + weight
        elif dhcptype == 'Decline' and ipttl != None:
          if ipttl in DeclineTTLPartialList:
            oldValue = DeclineTTLPartialList.get(ipttl)
            DeclineTTLPartialList[ipttl] = oldValue + '|' + os + ':' + weight
          else:
            DeclineTTLPartialList[ipttl] = os + ':' + weight

  return [DiscoverOptionsExactList, DiscoverOptionsPartialList, RequestOptionsExactList, RequestOptionsPartialList, ReleaseOptionsExactList, ReleaseOptionsPartialList, ACKOptionsExactList, ACKOptionsPartialList, AnyOptionsExactList, AnyOptionsPartialList, InformOptionsExactList, InformOptionsPartialList, DiscoverOption55ExactList, DiscoverOption55PartialList, RequestOption55ExactList, RequestOption55PartialList, ReleaseOption55ExactList, ReleaseOption55PartialList, ACKOption55ExactList, ACKOption55PartialList, AnyOption55ExactList, AnyOption55PartialList, InformOption55ExactList, InformOption55PartialList, DiscoverVendorCodeExactList, DiscoverVendorCodePartialList, RequestVendorCodeExactList, RequestVendorCodePartialList, ReleaseVendorCodeExactList, ReleaseVendorCodePartialList, ACKVendorCodeExactList, ACKVendorCodePartialList, AnyVendorCodeExactList, AnyVendorCodePartialList, InformVendorCodeExactList, InformVendorCodePartialList, DiscoverTTLExactList, DiscoverTTLPartialList, RequestTTLExactList, RequestTTLPartialList, ReleaseTTLExactList, ACKTTLExactList, AnyTTLExactList, InformTTLExactList, ACKTTLPartialList, AnyTTLPartialList, InformTTLPartialList, NAKOptionsPartialList, NAKOptionsExactList, NAKOption55PartialList, NAKOption55ExactList, NAKVendorCodePartialList, NAKVendorCodeExactList, NAKTTLPartialList, NAKTTLExactList, OfferOptionsPartialList, OfferOptionsExactList, OfferOption55PartialList, OfferOption55ExactList, OfferVendorCodePartialList, OfferVendorCodeExactList, OfferTTLPartialList, OfferTTLExactList, DeclineOptionsPartialList, DeclineOptionsExactList, DeclineOption55PartialList, DeclineOption55ExactList, DeclineVendorCodePartialList, DeclineVendorCodeExactList, DeclineTTLPartialList, DeclineTTLExactList]


def DHCPFingerprintLookup(exactList, partialList, value):
  exactValue = ''
  partialValue = ''

  if value in exactList:
    exactValue = exactList.get(value)

  for key, val in partialList.items():
    if value.find(key) > -1:
      partialValue = val

  fingerprint = exactValue + '|' + partialValue
  if fingerprint.startswith('|'):
    fingerprint = fingerprint[1:]
  if fingerprint.endswith('|'):
    fingerprint = fingerprint[:-1]

  return fingerprint


def getDHCPMessageType(value):
  res = ''

  if value == 1:
    res = "Request"
  elif value == 2:
    res = "Reply"
  else:
    res = "Unknown Message Type: " + value

  return (res)

def getDHCPOptions(value):
  options = ''
  option55 = ''
  vendorCode = ''
  messageType = ''

  for i in range(len(value)):
#    print ("%s" % (value[i]))
    try:
      options = options + str(value[i].type) + ','
      if value[i].type == 53:
        messageType = getDHCPOption53(value[i].body_bytes)
      if value[i].type == 55:
        option55 = getDHCPOption55(value[i].body_bytes)
      if value[i].type == 60:
        vendorCode = getDHCPOption60(value[i].body_bytes)
    except:
      pass

  if len(options) > 0:
    options = options[:-1]
  return (options, messageType, option55, vendorCode)


def getDHCPOption60(value):
  res = ''
  try:
    res = value.decode("utf-8", "strict")
    # get rid of any buffer garbage that is in some of the vendorcodes
    res = res.replace('\x00', '')
  except:
    res = value
  return (res)


def getDHCPOption55(value):
  res = ''
  for i in range(len(value)):
    res = res + str(value[i]) + ','

  if len(res) > 0:
    res = res[:-1]

  return (res)

def getDHCPOption53(value):
  res = ''
  value = ord(value)  #may be able to do it with Binary instead, but quick fix for now

  if value == 1:
    res = "Discover"
  elif value == 2:
    res = "Offer"
  elif value == 3:
    res = "Request"
  elif value == 4:
    res = "Decline"
  elif value == 5:
    res = "ACK"
  elif value == 6:
    res = "NAK"
  elif value == 7:
    res = "Release"
  elif value == 8:
    res = "Inform"
  else:
    res = "Unknown Option Message Type: " + value

  return(res)



