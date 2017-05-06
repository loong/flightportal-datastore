CREATE TABLE prices
(QuoteId integer, MinPrice decimal(6, 2), Direct boolean, Origin varchar, Destination varchar, OutboundDepartureTime timestamp,
OutboundCarriers varchar[], InboundDepartureTimes timestamp, InboundCarriers varchar[], QuoteTime timestamp, currency
char(3));
