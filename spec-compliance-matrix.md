# Compliance of Implementations with Specification

The following tables show which features are implemented by each OpenTelemetry
language implementation.

`+` means the feature is supported, `-` means it is not supported, `N/A` means
the feature is not applicable to the particular language, blank cell means the
status of the feature is not known.

## All Features

| Feature | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|Feature|Go|Java|JS|Python|Ruby|Erlang|PHP|Rust|C++|.NET|Swift|
| A Metric Producer Accepts An Optional Metric Filter |  |  |  |  |  | - |  |  |  |  |  |
| A Specified Resource Can Be Associated With All The Produced Metrics From Any Meter From The Meterprovider | + | + | + | + |  |  | + | + | + | + |  |
| A Valid Instrument Must Be Created And Warning Should Be Emitted When Multiple Instruments Are Registered Under The Same Meter Using The Same Name |  | + | + | + |  | + |  |  |  |  |  |
| Add Event | + | + | + | + | + | + | + | + | + | + | + |
| Add Order Preserved | + | + | + | + | + | + | + | + | + | + | + |
| All Methods Of Any Instrument Are Safe To Be Called Concurrently | + | + | + | - |  | + |  |  | + | + |  |
| All Methods Of Meter Are Safe To Be Called Concurrently | + | + | + | - |  | + |  |  | + | + |  |
| All Methods Of Meterprovider Are Safe To Be Called Concurrently | + | + | + | - |  | + |  |  | + | + |  |
| An Exemplarreservoir Has An Offer Method With Access To The Measurement Value Attributes Context And Timestamp |  | - |  | - |  | + | + |  |  | - |  |
| Array Attributes | + | + | + | + | + | + | + | + | + | + | + |
| Array Of Primitives | + | + | + | + | + | + | + | + | + | + | + |
| Associate Meter With Instrumentationscope |  | + | + | + |  | + |  | + | + |  |  |
| Associate Tracer With Instrumentation Scope |  |  |  | + |  |  | + |  |  |  |  |
| Asynchronouscounter Instrument Is Supported | + | + | + | + |  | + | + | + | + | + |  |
| Asynchronousgauge Instrument Is Supported | + | + | + | + |  | + | + | + | + | + |  |
| Asynchronousupdowncounter Instrument Is Supported | + | + | + | + |  | + | + | + | + | + |  |
| Attach Context | N/A | + | + | + | + | + | + | + | + | - | - |
| Attribute Collection Size Limit | + | + | + | + | + | + | + | + | - | - | + |
| Attribute Limits |  | + |  | + | + | + | + |  |  |  |  |
| Attributes Keys Are Sanitized | + | + | + | + | - | - | - | + | + | + | + |
| B3 Propagator | + | + | + | + | + | + | + | + | + | + | + |
| Basic Support | + | + | + | + | + | + | + | + | + | + | + |
| Batch Log Record Processor |  | + |  | + |  |  | + |  | + |  |  |
| Boolean Attributes | + | + | + | + | + | + | + | + | + | + | + |
| Boolean Type | + | + | + | + | + | + | + | + | + | + | + |
| Builtin Span Processors Implement Force Flush |  | + |  | + | + | + | + | + | + | + |  |
| Colliding Sanitized Attribute Keys Are Merged | + | + | - | - | - | - | - | + | - | - | - |
| Composite Propagator | + | + | + | + | + | + | + | + | + | + | + |
| Composite Sampler And Composable Samplers |  |  |  |  |  |  |  |  |  |  |  |
| Concurrent Sending | - | + | + |  |  | - |  | + | - | - | - |
| Configuration Is Managed Solely By The Meterprovider | + | + | + | + |  | + | + | + | + | + |  |
| Counter Instrument Is Supported | + | + | + | + |  | + | + | + | + | + |  |
| Create Context Key | + | + | + | + | + | + | + | + | + | + | + |
| Create Empty | + | + | + | + | + | + | + | + | + | + | + |
| Create From Attributes | + | + | + | + | + | + | + | + | + | + | + |
| Create New Span | + | + | + | + | + | + | + | + | + | + | + |
| Create Root Span | + | + | + | + | + | + | + | + | + | + | + |
| Create Tracer Provider | + | + | + | + | + | + | + | + | + | + | + |
| Create With Default Parent | N/A | + | + | + | + | + | + | + | + | + | + |
| Create With Parent From Context | + | + | + | + | + | + | + | + | + | + | + |
| Cumulative Histograms Become Prometheus Histograms | + | + | + | + | - | - | - | + | + | + | + |
| Cumulative Monotonic Sums Become Prometheus Counters | + | + | + | + | - | - | - | + | + | + | + |
| Cumulative Nonmonotonic Sums Become Prometheus Gauges | + | + | + | + | - | - | - | + | + | + | - |
| Custom Log Record Exporter |  | + |  | + |  |  | + |  | + |  |  |
| Custom Log Record Processor |  | + |  | + |  |  | + |  | + |  |  |
| Default Value Service Name | + | + |  | + | + | + | + |  | + | + |  |
| Delta Histograms Become Cumulative Prometheus Histograms | - | - | - | - | - | - | - | - | - | - | - |
| Delta Nonmonotonic Sums Become Cumulative Prometheus Counters | - | - | - | - | - | - | - | - | - | - | - |
| Detach Context | N/A | + | + | + | + | + | + | + | + | - | - |
| Documentation Adding Attributes Preferred |  |  |  | + | + |  | + |  |  | + |  |
| Double Floating Point Type | + | + | + | + | + | + | - | + | + | + | + |
| Duplicate Instrument Registration Name Conflicts Are Resolved By Using The Firstseen For The Stream Name |  | + |  |  |  | + |  |  |  |  |  |
| End | + | + | + | + | + | + | + | + | + | + | + |
| End With Timestamp | + | + | + | + | + | + | + | + | + | + | + |
| Error Status Mapping | + | + |  | + | + | - | + | + | + | + | - |
| Event Attributes Mapping To Annotations | + | + | + | + | + | + | + | + | + | + | + |
| Events Collection Size Limit | + | + | + | + | + | + | + | + | - | - | + |
| Events Safe Concurrent Calls | + | + | + | + | + | + | + | + | + | + | + |
| Exemplar Sampling Can Be Disabled |  | - |  | - |  | + |  |  |  | + |  |
| Exemplars Contain The Associated Trace Id And Span Id Of The Active Span In The Context When The Measurement Was Taken |  | + |  | - |  | + |  |  |  | + |  |
| Exemplars Contain The Timestamp When The Measurement Was Taken |  | + |  | - |  | + |  |  |  | + |  |
| Exemplars For Histograms And Monotonic Sums | - | - | - | - | - | - | - | - | - | - | - |
| Exemplars Retain Any Attributes Available In The Measurement That Are Not Preserved By Aggregation Or View Configuration |  | + |  | - |  | + |  |  |  | + |  |
| Exporter Interface |  | + |  | + | + | + | + | + | + | + |  |
| Exporter Interface Has Forceflush |  | + |  | + | + | + | + | - |  | + |  |
| Fetch Instrumentation Scope From Readable Span |  | + |  | + |  |  | + |  |  |  |  |
| Fields | + | + | + | + | + | + | + | + | + | + | + |
| Force Flush Sdk Only | + | + | - | + | + | + | + | + | + | + | + |
| Gauge Instrument Is Supported | - | - | - | + |  | - | - | + | - | - |  |
| Gauges Become Prometheus Gauges | + | + | + | + | - | - | - | + | + | + | - |
| Get Current Context | N/A | + | + | + | + | + | + | + | + | + | + |
| Get Meter Accepts Attributes 1 |  |  |  | + |  |  | + | + | + |  |  |
| Get Meter Accepts Name Version And Schema Url | + | + | + | + |  | + | + | + | + | - |  |
| Get Tracer | + | + | + | + | + | + | + | + | + | + | + |
| Get Tracer With Schema Url | + | + |  | + |  |  | + |  | + |  |  |
| Get Tracer With Scope Attributes |  |  |  | + |  |  | + |  | + |  |  |
| Get Value From Context | + | + | + | + | + | + | + | + | + | + | + |
| Getter Argument | N/A | + | + | + | + | + | + | N/A | + | + | + |
| Getter Argument Returning Keys | N/A | + | + | + | + | + | + | N/A | + | - | + |
| Global Propagator | + | + | + | + | + | + | + | + | + | + | + |
| Help Metadata | + | + | + | + | - | - | - | + | + | + | + |
| Histogram Instrument Is Supported | + | + | + | + |  | + | + | + | + | + |  |
| Honors Nonretryable Responses | + | - | - | + | + | - |  |  | - | - | - |
| Honors Retryable Responses With Backoff | + | - | + | + | + | - |  |  | - | - | - |
| Honors The User Agent Spec |  |  |  |  |  |  | + |  |  | + |  |
| Honors Throttling Response | + | - | - | + | + | - |  |  | - | - | - |
| Id Generators | + | + |  | + | + | + | + | + | + |  | + |
| Inmemory Mock Exporter | + | + | + | + | + | + | + | - | + | + | + |
| Instrument Descriptions Conform To The Specified Syntax | - | + |  | - |  | - |  |  | - | + |  |
| Instrument Names Conform To The Specified Syntax | + | + | + | + |  | + |  |  | + |  |  |
| Instrument Supports The Advisory Attributes Parameter |  | + |  |  |  | - |  |  |  |  |  |
| Instrument Supports The Advisory Explicitbucketboundaries Parameter |  | + |  |  |  | + |  |  |  |  |  |
| Instrument Units Conform To The Specified Syntax | - | + |  | + |  | - |  | + | + | + |  |
| Instrumentationlibrary Mapping | + | + | - | + | + | - | + | + | + | + | + |
| Instrumentationscope Mapping |  | + |  |  |  |  |  |  |  |  |  |
| Instruments Have An Optional Description | + | + | + | + |  | + | + | + | + | + |  |
| Instruments Have An Optional Unit Of Measure | + | + | + | + |  | + | + | + | + | + |  |
| Instruments Have Kind | + | + | + | + |  | + | + | + | + | + |  |
| Instruments Have Name | + | + | + | + |  | + | + | + | + | + |  |
| Integer Microseconds In Timestamps | N/A | + |  | + | + | - | + | + | + | + | + |
| Is Recording | + | + | + | + | + | + | + | + | + | + | + |
| Is Recording False After End | + | + | + | + | + | + | + | + | + | - | + |
| Is Remote | + | + | + | + | + | + | + | + | + | + | + |
| Is Valid | + | + | + | + | + | + | + | + | + | + | + |
| It Is Possible To Create Any Number Of Meterproviders | + | + | + | + |  | + | + | + | + | + |  |
| It Is Possible To Register Two Instruments With Same Name Under Different Meters | + | + | + | + |  | + |  | + | + | + |  |
| Jaeger Propagator | + | + | + | + | + | + | + | + | + | - | + |
| Links After Span Creation | + |  |  | + |  |  |  |  | + | + |  |
| Links Collection Size Limit | + | + | + | + | + | + | + | + | - | - | + |
| Links On Span Creation | + | + |  | + | + | + | + | + | + | + |  |
| Links Order Preserved | + | + |  | + | + | + | + | + | + | + |  |
| Logger Emit Log Record |  | + |  | + |  |  | + |  | + | - |  |
| Logger Provider Force Flush |  | + |  | + |  |  | + |  | + | - |  |
| Logger Provider Get Logger |  | + |  | + |  |  | + |  | + | - |  |
| Logger Provider Get Logger Accepts Attributes |  |  |  | + |  |  | + |  | + |  |  |
| Logger Provider Shutdown |  | + |  | + |  |  | + |  | + | - |  |
| Loggerenabled | + |  |  |  |  |  |  | + | + |  |  |
| Logrecordprocessorenabled | + |  |  |  |  |  |  | + |  |  |  |
| Logrecordset Eventname | + |  |  |  |  |  |  | + | + |  |  |
| Mark Span Active | N/A | + | + | + | + | + | + | + | + | + | + |
| Merge V2 | + | + |  | + | + | + | + | + | + | + |  |
| Meterprovider Allows A Resource To Be Specified | + | + | + | + |  |  | + | + | + | + |  |
| Meterprovider Provides A Way To Get A Meter | + | + | + | + |  | + | + | + | + | - |  |
| Metric Exporter Configurable Default Aggregation |  | + |  | + |  |  |  |  |  |  |  |
| Metric Exporter Configurable Temporality Preference |  | + |  | + |  |  |  |  |  |  |  |
| Metric Sdk Implements Cardinality Limit |  | + | + | - |  |  |  | - | + | + |  |
| Metric Sdk Supports Configuring Cardinality Limit At Meterreader Level |  | + | + | - |  |  |  | - | - | - |  |
| Metric Sdk Supports Configuring Cardinality Limit Per Metric Using Views |  | + | + | - |  |  |  | - | - | + |  |
| Multidestination Spec Compliance | + | - |  |  |  | - |  |  | - | - | - |
| New Span Id For Non Recording Spans | + | + |  | + | + | + | + | + | + | - | + |
| No Explicit Parent Allowed | + | + | + | + | + | + | + | + | + | - | + |
| Null Values Documented Invalid | + | + | + | + | + | N/A | + |  | + |  | N/A |
| Opencensus Binary Propagator | + |  |  |  |  |  |  |  |  |  |  |
| Opentracing Span |  |  |  |  |  |  |  |  |  |  |  |
| Opentracing Tracer |  |  |  |  |  |  |  |  |  |  |  |
| Ot Propagator | + | + | + | + |  |  |  |  |  |  |  |
| Otel Scope Attribute Labels On All Metricsspecificationcompatibilityprometheus And Openmetricsmdinstrumentationscope1 | + | - | - | - | - | - | - | - | - | - | - |
| Otel Scope Labels Can Be Disabled | + | - | - | - | - | - | - | + | - | - | - |
| Otel Scope Name And Otel Scope Version Labels On All Metrics | + | + | - | - | - | - | - | + | - | - | - |
| Otlp File Exporter |  | - |  | - |  |  |  |  | + | - |  |
| Otlp Grpc Exporter | + | + | + | + |  | + | + | + | + | + | + |
| Otlp Http Binary Protobuf Exporter | + | + | + | + | + | + | + | + | + | + | - |
| Otlp Http Exporter |  | + |  | + |  |  | + |  | + | + |  |
| Otlp Http Gzip Content Encoding | + | + | + | + | + | - | + |  | - | - | - |
| Otlp Http Json Protobuf Exporter | + | - | + |  |  | - | + |  | + | - | - |
| Partial Success Messages Are Handled And Logged For Otlpgrpc | + |  |  |  |  |  | + |  |  |  |  |
| Partial Success Messages Are Handled And Logged For Otlphttp | + |  |  |  |  |  | + |  |  |  |  |
| Prometheus Counters Have Total Suffix By Default | + | + | + | + | - | - | - | + | - | - | - |
| Prometheus Counters Total Suffixing Can Be Disabled | + | - | - | - | - | - | - | - | - | - | - |
| Prometheus Metadata Deduplication | + | + | - | - | - | - | - | + | - | - | - |
| Prometheus Name Sanitization | + | + | + | + | - | - | - | + | + | + | + |
| Record Exception | - | + | + | + | + | + | + | + | - | + | - |
| Record Exception With Extra Parameters | - | + | + | + | + | + | + | + | - | + | - |
| Resource Detector Interface | + | + | + | + | + | + | + | + | + | + | + |
| Resource Detectors Populate Schema Url | + | + |  |  |  | - | + |  |  | - |  |
| Retrieve Attributes | + | + | + | + | + | + | + | + | + | + | + |
| Reuse Standard Attributes | + |  |  |  |  |  |  |  |  |  |  |
| Sampler Jaeger Remote Sampler | + | + |  |  |  |  |  | + |  |  |  |
| Samplers Modify Tracestate | + | + |  | + | + | + | + | + | + | + | + |
| Sampling |  |  |  |  |  |  |  |  |  |  |  |
| Schemaurl In Resourcelogs And Scopelogs |  | + |  | + |  | - | + |  |  | - |  |
| Schemaurl In Resourcemetrics And Scopemetrics |  | + |  | + |  | - | + |  |  | - |  |
| Schemaurl In Resourcespans And Scopespans | + | + |  | + |  | + | + |  |  | - |  |
| Service Name Mapping | + | + | + | + | + | + | + | + | + | + | + |
| Set Active Span | N/A | + | + | + | + | + | + | + | + | + | + |
| Set Attribute | + | + | + | + | + | + | + | + | + | + | + |
| Set Order Preserved | + | - | + | + | + | + | + | + | + | + | + |
| Set Status With Status Code | + | + | + | + | + | + | + | + | + | + | + |
| Set Value For Context | + | + | + | + | + | + | + | + | + | + | + |
| Setter Argument | N/A | + | + | + | + | + | + | N/A | + | + | + |
| Should Sample Gets Full Parent Context | + | + | + | + | + | + | + | + | + | - | + |
| Shutdown Sdk Only | + | + | + | + | + | + | + | + | + | + | + |
| Signed Int64 Type | + | + | + | + | + | + | - | + | + | + | + |
| Simple Log Record Processor |  | + |  | + |  |  | + |  | + |  |  |
| Span Attributes |  |  |  |  |  |  |  |  |  |  |  |
| Span Events |  |  |  |  |  |  |  |  |  |  |  |
| Span Exceptions |  |  |  |  |  |  |  |  |  |  |  |
| Span Limits | + | + |  | + | + | + | + |  | - |  | + |
| Span Linking |  |  |  |  |  |  |  |  |  |  |  |
| Span Processor On Ending | - | - | - | - | - | - | - | - | - | - | - |
| Span Processor Onstart Receives Parent Context | + | + | + | + | + | + | + | + | - | - | + |
| Spancontext |  |  |  |  |  |  |  |  |  |  |  |
| Spankind Mapping | + | + | + | + | + | + | + | + | + | + | + |
| Standard Output Logging | + | + | + | + | + | + | + | + | + | + | + |
| Status Mapping | + | + | + | + | + | + | + | + | + | + | + |
| String Type | + | + | + | + | + | + | + | + | + | + | + |
| Support W3C Trace Context Level2 Randomness |  |  |  |  |  |  |  |  |  |  |  |
| Target Info Metric From Resource | + | + | + | + | - | - | - | + | - | - | - |
| Textmap Propagator | + | + |  | + | + |  | + |  | + |  |  |
| The Api Provides A Way To Set And Get A Global Default Meterprovider | + | + | + | + |  | + | + | + | + | - |  |
| The Default Aggregation Is Available | + | + | + | + |  | + |  | + | + | + |  |
| The Default Aggregation Uses The Specified Aggregation By Instrument | + | + | + | + |  | + |  | + | + | + |  |
| The Drop Aggregation Is Available | + | + | + | + |  | + |  | + | + | + |  |
| The Explicitbuckethistogram Aggregation Is Available | - | + | + | + |  | + | + | + | + | + |  |
| The Exponentialbuckethistogram Aggregation Is Available |  |  |  | + |  |  |  |  |  | + |  |
| The Fallback Meter Name Property Keeps Its Original Invalid Value | - | - | + | + |  | + |  | + | - | - |  |
| The Lastvalue Aggregation Is Available | + | + | + | + |  | + | + | + | + | + |  |
| The Meterprovider Provides Methods To Update The Configuration | - | - | - | + |  | - |  |  | - | + |  |
| The Metric Reader Implementation Supports Registering Metric Filter And Passing Them Its Registered Metric Producers |  |  |  |  |  | - |  |  |  |  |  |
| The Metric Sdks Metric Producer Implementations Uses The Metric Filter |  |  |  |  |  | - |  |  |  |  |  |
| The Metrics Exporter Export Function Can Not Be Called Concurrently From The Same Exporter Instance | + | + | + | - |  | + |  |  | + | + |  |
| The Metrics Exporter Export Function Does Not Block Indefinitely | + | + | + | - |  | + |  |  | + | + |  |
| The Metrics Exporter Export Function Receives A Batch Of Metrics | + | + | + | + |  | + | + | + | + | + |  |
| The Metrics Exporter Export Function Returns Success Or Failure | + | + | + | + |  | + | + | + | + | + |  |
| The Metrics Exporter Forceflush Can Inform The Caller Whether It Succeeded Failed Or Timed Out |  | + | + | + |  | + | + |  | + | + |  |
| The Metrics Exporter Has Access To The Aggregated Metrics Data Aggregated Points Not Raw Measurements | + | + | + | + |  | + |  | + | + | + |  |
| The Metrics Exporter Provides A Forceflush Function | - | + | + | + |  | + | + | + | + | + |  |
| The Metrics Exporter Provides A Shutdown Function | + | + | + | + |  | + | + | + | + | + |  |
| The Metrics Exporter Shutdown Function Do Not Block Indefinitely | + | + | + | - |  | + |  |  | + | + |  |
| The Metrics Reader Implementation Supports Configuring The Default Aggregation On The Basis Of Instrument Kind |  | + |  | + |  | + |  |  | - | - |  |
| The Metrics Reader Implementation Supports Configuring The Default Temporality On The Basis Of Instrument Kind |  | + | + | + |  | + |  | + | + |  |  |
| The Metrics Reader Implementation Supports Registering Metric Exporters |  | + | + | + |  | + | + | + | + | + |  |
| The Metrics Sdk Provides A Simplefixedsizeexemplarreservoir That Is Used By Default For All Aggregations Except Explicitbuckethistogram |  | + |  | - |  | + | + |  |  | - |  |
| The Metrics Sdk Provides An Alignedhistogrambucketexemplarreservoir That Is Used By Default For Explicitbuckethistogram Aggregation |  | + |  | - |  | + |  |  |  | - |  |
| The Metrics Sdk Provides An Exemplarreservoir Interface Or Extension Point |  | - |  | - |  | + | + |  |  | - |  |
| The Metrics Sdk Samples Exemplars From Measurements |  | + |  | - |  | + |  |  |  | + |  |
| The Metrics Sdk Supports Alwaysoff Exemplar Filter |  | + |  | - |  | + |  |  |  | + |  |
| The Metrics Sdk Supports Alwayson Exemplar Filter |  | + |  | - |  | + |  |  |  | + |  |
| The Metrics Sdk Supports Sdkwide Exemplar Filter Configuration |  | + |  | - |  | + |  |  |  | + |  |
| The Metrics Sdk Supports Tracebased Exemplar Filter |  | + |  | - |  | + |  |  |  | + |  |
| The Name Of The View Can Be Specified |  | + | + | + |  | + | + |  | + | + |  |
| The Sdk Allows More Than One View To Be Specified Per Instrument |  | + | + | + |  | + |  | + | + | + |  |
| The Sum Aggregation Is Available | + | + | + | + |  | + | + | + | + | + |  |
| The Supplied Name Version And Schema Url Arguments Passed To The Meterprovider Are Used To Create An Instrumentationlibrary Instance Stored In The Meter | + | - |  | + |  |  |  | + | + | - |  |
| The Supplied Name Version And Schema Url Arguments Passed To The Meterprovider Are Used To Create An Instrumentationscope Instance Stored In The Meter |  | + | + | + |  | + | + | + | + |  |  |
| The Updated Configuration Applies To All Already Returned Meters | - | - | - | - |  | - |  |  | - | + |  |
| The View Allows Configuring Excluded Attribute Keys Of Resulting Metric Stream | + |  |  |  |  |  |  |  |  |  |  |
| The View Allows Configuring The Exemplar Reservoir Of Resulting Metric Stream |  | - |  | - |  | - |  |  |  | - |  |
| The View Allows Configuring The Name Description Attributes Keys And Aggregation Of The Resulting Metric Stream |  | + | + | + |  | + | + | + | + | - |  |
| The View Instrument Selection Criteria Is As Specified |  | + | + | + |  | + | + | + | + | + |  |
| The View Instrument Selection Criteria Supports The Matchall Wildcard |  | + | + | + |  | + |  | + | + | + |  |
| The View Instrument Selection Criteria Supports Wildcards |  | + | + | + |  | - |  | + | + | + |  |
| There Is A Way To Register Views With A Meterprovider | - | + | + | + |  | + | + | + | + | + |  |
| Trace Context Injection |  | + |  | + |  |  | + |  | + | + |  |
| Trace Context Interaction |  |  |  |  |  |  |  |  |  |  |  |
| Trace Context Propagator | + | + | + | + | + | + | + | + | + | + | + |
| Traceid Ratio Based Sampler Th Field |  |  |  |  |  |  |  |  |  |  |  |
| Tracer Get Active Span | N/A | + | + | + | + | + | + | + | + | + | + |
| Tracerprovider |  |  |  |  |  |  |  |  |  |  |  |
| Type Metadata | + | + | + | + | - | - | - | + | + | + | + |
| Unicode Support | + | + | + | + | + | + | + | + | + | + | + |
| Unit Full Words | + | + | - | - | - | - | - | + | - | - | - |
| Unit Metadata | - | - | + | + | - | - | - | - | - | + | - |
| Unit Suffixes | + | + | - | + | - | - | - | + | + | + | - |
| Update Name | + | + | + | + | + | + | + | + | + | + | + |
| Updowncounter Instrument Is Supported | + | + | + | + |  | + | + | + | + | + |  |
| Use Official Header Name | + | + | + | + | + | + | + | + | + | + | + |
| User Defined Start Timestamp | + | + | + | + | + | + | + | + | + | + | + |
| W3C Tracecontext Spec | + | + | + | + | + | + | + | + | + | + | + |
| When An Invalid Name Is Specified A Working Meter Implementation Is Returned As A Fallback | + | + | + | + |  | + |  | + | + | - |  |
| Zipkin V1 Json | - | + |  | + | - | - | - | - | - | - | - |
| Zipkin V1 Thrift | - | + |  |  | - | - | - | - | - | - | - |
| Zipkin V2 Json | + | + |  | + | + | - | + | + | + | + | + |
| Zipkin V2 Protobuf | - | + |  | + | - | + | - | - | - | - | - |
