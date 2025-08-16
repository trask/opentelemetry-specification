# Compliance of Implementations with Specification

The following tables show which features are implemented by each OpenTelemetry
language implementation.

## Legend

### Implementation Status

- `+` means the feature is supported and stable in the language implementation
- `-` means the feature is not supported
- `🧪` means the feature has experimental support in the language implementation
- `N/A` means the feature is not applicable to the particular language
- blank cell means the status of the feature is not known

### Specification Status

- Features marked with `🚧` are experimental in the specification
- Features marked with `⚠️` are deprecated in the specification
- Features with no symbol are stable in the specification

## Traces

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| [TracerProvider](specification/trace/api.md#tracerprovider-operations) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Create TracerProvider |  | + | + | + | + | + | + | + | + | + | + | + |
| Get a Tracer |  | + | + | + | + | + | + | + | + | + | + | + |
| Get a Tracer with schema_url |  | + | + |  | + |  |  | + |  | + |  |  |
| Get a Tracer with scope attributes |  |  |  |  | + |  |  | + |  | + |  |  |
| Associate Tracer with InstrumentationScope |  |  |  |  | + |  |  | + |  |  |  |  |
| Safe for concurrent calls |  | + | + | + | + | + | + | + | + | + | + | + |
| Shutdown (SDK only required) |  | + | + | + | + | + | + | + | + | + | + | + |
| ForceFlush (SDK only required) |  | + | + | - | + | + | + | + | + | + | + | + |
| [Trace / Context interaction](specification/trace/api.md#context-interaction) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Get active Span |  | N/A | + | + | + | + | + | + | + | + | + | + |
| Set active Span |  | N/A | + | + | + | + | + | + | + | + | + | + |
| [Tracer](specification/trace/api.md#tracer-operations) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Create a new Span |  | + | + | + | + | + | + | + | + | + | + | + |
| Documentation defines adding attributes at span creation as preferred |  |  |  |  | + | + |  | + |  |  | + |  |
| Get active Span |  | N/A | + | + | + | + | + | + | + | + | + | + |
| Mark Span active |  | N/A | + | + | + | + | + | + | + | + | + | + |
| Safe for concurrent calls |  | + | + | + | + | + | + | + | + | + | + | + |
| [SpanContext](specification/trace/api.md#spancontext) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| IsValid |  | + | + | + | + | + | + | + | + | + | + | + |
| IsRemote |  | + | + | + | + | + | + | + | + | + | + | + |
| Conforms to the W3C TraceContext spec |  | + | + | + | + | + | + | + | + | + | + | + |
| [Span](specification/trace/api.md#span) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Create root span |  | + | + | + | + | + | + | + | + | + | + | + |
| Create with default parent (active span) |  | N/A | + | + | + | + | + | + | + | + | + | + |
| Create with parent from Context |  | + | + | + | + | + | + | + | + | + | + | + |
| No explicit parent Span/SpanContext allowed |  | + | + | + | + | + | + | + | + | + | - | + |
| SpanProcessor.OnStart receives parent Context |  | + | + | + | + | + | + | + | + | - | - | + |
| UpdateName |  | + | + | + | + | + | + | + | + | + | + | + |
| User-defined start timestamp |  | + | + | + | + | + | + | + | + | + | + | + |
| End |  | + | + | + | + | + | + | + | + | + | + | + |
| End with timestamp |  | + | + | + | + | + | + | + | + | + | + | + |
| IsRecording |  | + | + | + | + | + | + | + | + | + | + | + |
| IsRecording becomes false after End |  | + | + | + | + | + | + | + | + | + | - | + |
| Set status with StatusCode (Unset, Ok, Error) |  | + | + | + | + | + | + | + | + | + | + | + |
| Safe for concurrent calls |  | + | + | + | + | + | + | + | + | + | + | + |
| events collection size limit |  | + | + | + | + | + | + | + | + | - | - | + |
| attribute collection size limit |  | + | + | + | + | + | + | + | + | - | - | + |
| links collection size limit |  | + | + | + | + | + | + | + | + | - | - | + |
| [SpanProcessor.OnEnding](specification/trace/sdk.md#onending) | X | - | - | - | - | - | - | - | - | - | - | - |
| [Span attributes](specification/trace/api.md#set-attributes) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| SetAttribute |  | + | + | + | + | + | + | + | + | + | + | + |
| Set order preserved | X | + | - | + | + | + | + | + | + | + | + | + |
| String type |  | + | + | + | + | + | + | + | + | + | + | + |
| Boolean type |  | + | + | + | + | + | + | + | + | + | + | + |
| Double floating-point type |  | + | + | + | + | + | + | - | + | + | + | + |
| Signed int64 type |  | + | + | + | + | + | + | - | + | + | + | + |
| Array of primitives (homogeneous) |  | + | + | + | + | + | + | + | + | + | + | + |
| `null` values documented as invalid/undefined |  | + | + | + | + | + | N/A | + |  | + |  | N/A |
| Unicode support for keys and string values |  | + | + | + | + | + | + | + | + | + | + | + |
| [Span linking](specification/trace/api.md#specifying-links) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Links can be recorded on span creation |  | + | + |  | + | + | + | + | + | + | + |  |
| Links can be recorded after span creation |  | + |  |  | + |  |  |  |  | + | + |  |
| Links order is preserved |  | + | + |  | + | + | + | + | + | + | + |  |
| [Span events](specification/trace/api.md#add-events) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| AddEvent |  | + | + | + | + | + | + | + | + | + | + | + |
| Add order preserved |  | + | + | + | + | + | + | + | + | + | + | + |
| Safe for concurrent calls |  | + | + | + | + | + | + | + | + | + | + | + |
| [Span exceptions](specification/trace/api.md#record-exception) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| RecordException |  | - | + | + | + | + | + | + | + | - | + | - |
| RecordException with extra parameters |  | - | + | + | + | + | + | + | + | - | + | - |
| [Sampling](specification/trace/sdk.md#sampling) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Allow samplers to modify tracestate |  | + | + |  | + | + | + | + | + | + | + | + |
| ShouldSample gets full parent Context |  | + | + | + | + | + | + | + | + | + | - | + |
| Sampler: JaegerRemoteSampler |  | + | + |  |  |  |  |  | + |  |  |  |
| [New Span ID created also for non-recording Spans](specification/trace/sdk.md#sdk-span-creation) |  | + | + |  | + | + | + | + | + | + | - | + |
| [IdGenerators](specification/trace/sdk.md#id-generators) |  | + | + |  | + | + | + | + | + | + |  | + |
| [SpanLimits](specification/trace/sdk.md#span-limits) | X | + | + |  | + | + | + | + |  | - |  | + |
| [Built-in `SpanProcessor`s implement `ForceFlush` spec](specification/trace/sdk.md#forceflush-1) |  |  | + |  | + | + | + | + | + | + | + |  |
| [Attribute Limits](specification/common/README.md#attribute-limits) | X |  | + |  | + | + | + | + |  |  |  |  |
| Fetch InstrumentationScope from ReadableSpan |  |  | + |  | + |  |  | + |  |  |  |  |
| [Support W3C Trace Context Level 2 randomness](specification/trace/sdk.md#traceid-randomness) 🚧 | X |  |  |  |  |  |  |  |  |  |  |  |
| [TraceIdRatioBased sampler implements OpenTelemetry tracestate `th` field](specification/trace/sdk.md#traceidratiobased) 🚧 | X |  |  |  |  |  |  |  |  |  |  |  |
| [CompositeSampler and built-in ComposableSamplers](specification/trace/sdk.md#compositesampler) 🚧 | X |  |  |  |  |  |  |  |  |  |  |  |

## Baggage

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| Baggage Basic Support |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Basic support |  | + | + | + | + | + | + | + | + | + | + | + |
| Use official header name `baggage` |  | + | + | + | + | + | + | + | + | + | + | + |

## Metrics

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| MeterProvider |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| The API provides a way to set and get a global default `MeterProvider` | X | + | + | + | + |  | + | + | + | + | - |  |
| It is possible to create any number of `MeterProvider`s | X | + | + | + | + |  | + | + | + | + | + |  |
| `MeterProvider` provides a way to get a `Meter` |  | + | + | + | + |  | + | + | + | + | - |  |
| `get_meter` accepts name, `version` and `schema_url` |  | + | + | + | + |  | + | + | + | + | - |  |
| `get_meter` accepts `attributes` |  |  |  |  | + |  |  | + | + | + |  |  |
| When an invalid `name` is specified a working `Meter` implementation is returned as a fallback |  | + | + | + | + |  | + |  | + | + | - |  |
| The fallback `Meter` `name` property keeps its original invalid value | X | - | - | + | + |  | + |  | + | - | - |  |
| Associate `Meter` with `InstrumentationScope` |  |  | + | + | + |  | + |  | + | + |  |  |
| Instruments |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| `Counter` instrument is supported |  | + | + | + | + |  | + | + | + | + | + |  |
| `AsynchronousCounter` instrument is supported |  | + | + | + | + |  | + | + | + | + | + |  |
| `Histogram` instrument is supported |  | + | + | + | + |  | + | + | + | + | + |  |
| `AsynchronousGauge` instrument is supported |  | + | + | + | + |  | + | + | + | + | + |  |
| `Gauge` instrument is supported 🚧 |  | - | - | - | + |  | - | - | + | - | - |  |
| `UpDownCounter` instrument is supported |  | + | + | + | + |  | + | + | + | + | + |  |
| `AsynchronousUpDownCounter` instrument is supported |  | + | + | + | + |  | + | + | + | + | + |  |

## Logs

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| [LoggerProvider](specification/logs/sdk.md) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| LoggerProvider.Get Logger |  |  | + |  | + |  |  | + |  | + | - |  |
| LoggerProvider.Get Logger accepts attributes |  |  |  |  | + |  |  | + |  | + |  |  |
| LoggerProvider.Shutdown |  |  | + |  | + |  |  | + |  | + | - |  |
| LoggerProvider.ForceFlush |  |  | + |  | + |  |  | + |  | + | - |  |
| Logger.Emit(LogRecord) |  |  | + |  | + |  |  | + |  | + | - |  |
| LogRecord Processors |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| SimpleLogRecordProcessor |  |  | + |  | + |  |  | + |  | + |  |  |
| BatchLogRecordProcessor |  |  | + |  | + |  |  | + |  | + |  |  |
| Can plug custom LogRecordProcessor |  |  | + |  | + |  |  | + |  | + |  |  |
| LogRecord Exporters |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| OTLP/gRPC exporter |  | + | + | + | + |  | + | + | + | + | + | + |
| OTLP/HTTP exporter |  |  | + |  | + |  |  | + |  | + | + |  |
| OTLP File exporter |  |  | - |  | - |  |  |  |  | + | - |  |
| Can plug custom LogRecordExporter |  |  | + |  | + |  |  | + |  | + |  |  |
| Trace Context Injection |  |  | + |  | + |  |  | + |  | + | + |  |

## Resource

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| Resource Operations |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Create from Attributes |  | + | + | + | + | + | + | + | + | + | + | + |
| Create empty |  | + | + | + | + | + | + | + | + | + | + | + |
| [Merge (v2)](specification/resource/sdk.md#merge) |  | + | + |  | + | + | + | + | + | + | + |  |
| Retrieve attributes |  | + | + | + | + | + | + | + | + | + | + | + |
| Default value for service.name |  | + | + |  | + | + | + | + |  | + | + |  |
| [Resource detector interface/mechanism](specification/resource/sdk.md#detecting-resource-information-from-the-environment) |  | + | + | + | + | + | + | + | + | + | + | + |
| [Resource detectors populate Schema URL](specification/resource/sdk.md#detecting-resource-information-from-the-environment) |  | + | + |  |  |  | - | + |  |  | - |  |

## Context Propagation

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| Context Operations |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Create Context Key |  | + | + | + | + | + | + | + | + | + | + | + |
| Get value from Context |  | + | + | + | + | + | + | + | + | + | + | + |
| Set value for Context |  | + | + | + | + | + | + | + | + | + | + | + |
| Attach Context |  | N/A | + | + | + | + | + | + | + | + | - | - |
| Detach Context |  | N/A | + | + | + | + | + | + | + | + | - | - |
| Get current Context |  | N/A | + | + | + | + | + | + | + | + | + | + |
| Propagators |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Composite Propagator |  | + | + | + | + | + | + | + | + | + | + | + |
| Global Propagator |  | + | + | + | + | + | + | + | + | + | + | + |
| TraceContext Propagator |  | + | + | + | + | + | + | + | + | + | + | + |
| B3 Propagator |  | + | + | + | + | + | + | + | + | + | + | + |
| Jaeger Propagator |  | + | + | + | + | + | + | + | + | + | - | + |
| OT Propagator |  | + | + | + | + |  |  |  |  |  |  |  |
| OpenCensus Binary Propagator |  | + |  |  |  |  |  |  |  |  |  |  |
| [TextMapPropagator](specification/context/api-propagators.md#textmap-propagator) |  | + | + |  | + | + |  | + |  | + |  |  |

## Environment Variables

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| Environment Variable Support | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| OTEL_SDK_DISABLED | X |  | + | - | + | - | - | + | - | - | - | - |
| OTEL_RESOURCE_ATTRIBUTES | X |  | + | + | + | + | + | + | + | + | + | - |
| OTEL_SERVICE_NAME | X |  | + | + | + | + | + | + |  | + | + |  |
| OTEL_LOG_LEVEL | X |  | - | + |  | + | - | + |  | - | - | - |
| OTEL_PROPAGATORS | X |  | + |  | + | + | + | + | - | - | - | - |

## Declarative Configuration

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| [Declarative Configuration](specification/configuration/README.md#declarative-configuration) 🚧 |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| `Parse` a configuration file 🚧 |  |  | 🧪 |  |  |  |  |  |  |  |  |  |
| The `Parse` operation accepts the configuration YAML file format 🚧 |  |  | 🧪 |  |  |  |  |  |  |  |  |  |
| The `Parse` operation performs environment variable substitution 🚧 |  |  | 🧪 |  |  |  |  |  |  |  |  |  |
| `Create` SDK components 🚧 |  |  | 🧪 |  |  |  |  |  |  |  |  |  |

## Exporters

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| [OTLP Exporters](specification/protocol/otlp.md) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| OTLP/gRPC Exporter |  | + | + | + | + |  | + | + | + | + | + | + |
| OTLP/HTTP binary Protobuf Exporter |  | + | + | + | + | + | + | + | + | + | + | - |
| OTLP/HTTP JSON Protobuf Exporter |  | + | - | + |  |  | - | + |  | + | - | - |
| OTLP/HTTP gzip Content-Encoding support | X | + | + | + | + | + | - | + |  | - | - | - |
| [Zipkin Exporters](specification/trace/sdk_exporters/zipkin.md) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| Zipkin V1 JSON | X | - | + |  | + | - | - | - | - | - | - | - |
| Zipkin V1 Thrift | X | - | + |  |  | - | - | - | - | - | - | - |
| Zipkin V2 JSON |  | + | + |  | + | + | - | + | + | + | + | + |
| Zipkin V2 Protobuf |  | - | + |  | + | - | + | - | - | - | - | - |
| Prometheus Exporters |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| [Metadata Deduplication](specification/compatibility/prometheus_and_openmetrics.md#metric-metadata-1) |  | + | + | - | - | - | - | - | + | - | - | - |
| [Name Sanitization](specification/compatibility/prometheus_and_openmetrics.md#metric-metadata-1) |  | + | + | + | + | - | - | - | + | + | + | + |

## Compatibility

| Feature | Optional | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
|-------|--------|---|----|---|------|----|------|---|----|---|----|-----|
| [OpenCensus Compatibility](specification/compatibility/opencensus.md) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| [Trace Bridge](specification/compatibility/opencensus.md#trace-bridge) |  |  | + | + | + |  | - |  |  | - | - |  |
| [Metric Bridge](specification/compatibility/opencensus.md#metrics--stats) |  |  | + | - | - |  | - |  |  | - | - |  |
| [OpenTracing Compatibility](specification/compatibility/opentracing.md) |  | Go | Java | JS | Python | Ruby | Erlang | PHP | Rust | C++ | .NET | Swift |
| [Create OpenTracing Shim](specification/compatibility/opentracing.md#create-an-opentracing-tracer-shim) |  |  |  |  |  |  |  | + |  |  |  |  |
| [Tracer](specification/compatibility/opentracing.md#tracer-shim) |  |  |  |  |  |  |  | + |  |  |  |  |
| [Span](specification/compatibility/opentracing.md#span-shim) |  | + |  |  |  |  | + | + |  |  |  |  |
