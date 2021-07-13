import asyncio
import os
def handler(event, context):
    return asyncio.get_event_loop().run_until_complete(async_handler(event))
    


async def async_handler(event):
    print('======================================================================')
    print('we receive the createPartyRegistration from VEN')
    print(event['body'])
    body = """<?xml version="1.0" encoding="UTF-8"?>
<!--Sample XML file generated by XMLSpy v2010 rel. 3 (x64) (http://www.altova.com)-->
<oadr:oadrPayload  xmlns:emix="http://docs.oasis-open.org/ns/emix/2011/06" xmlns:power="http://docs.oasis-open.org/ns/emix/2011/06/power" xmlns:scale="http://docs.oasis-open.org/ns/emix/2011/06/siscale" xmlns:ei="http://docs.oasis-open.org/ns/energyinterop/201110" xmlns:pyld="http://docs.oasis-open.org/ns/energyinterop/201110/payloads" xmlns:oadr="http://openadr.org/oadr-2.0b/2012/07" xmlns:n2="http://www.altova.com/samplexml/other-namespace" xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:xcal="urn:ietf:params:xml:ns:icalendar-2.0" xmlns:strm="urn:ietf:params:xml:ns:icalendar-2.0:stream">
	<oadr:oadrSignedObject>
		<oadr:oadrCreatedPartyRegistration ei:schemaVersion="2.0b">
			<ei:eiResponse>
				<ei:responseCode>200</ei:responseCode>
				<ei:responseDescription>OK</ei:responseDescription>
				<pyld:requestID>REQ_123</pyld:requestID>
			</ei:eiResponse>
			<ei:registrationID>REG_2222</ei:registrationID>
			<ei:venID>VEN_123</ei:venID>
			<ei:vtnID>VTN_1234</ei:vtnID>
			<oadr:oadrProfiles>
				<oadr:oadrProfile>
					<oadr:oadrProfileName>2.0a</oadr:oadrProfileName>
					<oadr:oadrTransports>
						<oadr:oadrTransport>
							<oadr:oadrTransportName>simpleHttp</oadr:oadrTransportName>
						</oadr:oadrTransport>
					</oadr:oadrTransports>
				</oadr:oadrProfile>
				<oadr:oadrProfile>
					<oadr:oadrProfileName>2.0b</oadr:oadrProfileName>
					<oadr:oadrTransports>
						<oadr:oadrTransport>
							<oadr:oadrTransportName>simpleHttp</oadr:oadrTransportName>
						</oadr:oadrTransport>
						<oadr:oadrTransport>
							<oadr:oadrTransportName>xmpp</oadr:oadrTransportName>
						</oadr:oadrTransport>
					</oadr:oadrTransports>
				</oadr:oadrProfile>
			</oadr:oadrProfiles>
			<oadr:oadrRequestedOadrPollFreq>
				<xcal:duration>PT5S</xcal:duration>
			</oadr:oadrRequestedOadrPollFreq>
			<oadr:oadrServiceSpecificInfo>
				<oadr:oadrService>
					<oadr:oadrServiceName>EiRegisterParty</oadr:oadrServiceName>
					<oadr:oadrInfo>
						<oadr:oadrKey>A Key</oadr:oadrKey>
						<oadr:oadrValue>A Value</oadr:oadrValue>
					</oadr:oadrInfo>
				</oadr:oadrService>
			</oadr:oadrServiceSpecificInfo>
			<oadr:oadrExtensions>
				<oadr:oadrExtension>
					<oadr:oadrExtensionName>My Extension</oadr:oadrExtensionName>
					<oadr:oadrInfo>
						<oadr:oadrKey>A Key</oadr:oadrKey>
						<oadr:oadrValue>A Value</oadr:oadrValue>
					</oadr:oadrInfo>
				</oadr:oadrExtension>
			</oadr:oadrExtensions>
		</oadr:oadrCreatedPartyRegistration>
	</oadr:oadrSignedObject>
</oadr:oadrPayload>
"""

    return {'status': 200,'body':body}