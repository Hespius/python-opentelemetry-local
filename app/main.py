import opentelemetry.trace as trace
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export import BatchSpanProcessor

tracer_provider = TracerProvider(
    resource=Resource.create({SERVICE_NAME: "teste"})
)

# Configurar o exportador Jaeger
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Endereço do agente Jaeger (pode variar)
    agent_port=6831,  # Porta padrão para comunicação com o agente Jaeger
)

span_processor = SimpleSpanProcessor(jaeger_exporter)
tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
# tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

tracer = trace.get_tracer(__name__)

# Função para realizar somas matemáticas
@tracer.start_as_current_span("sum")
def somar(a, b):
    resultado = a + b
    return subtrair(resultado, 10)

@tracer.start_as_current_span("sub")
def subtrair(a, b):
    return a - b


if __name__ == "__main__":
    # resultado = somar(10, 20)
    # resultado = somar(10, 20)
    # resultado = somar(10, 20)
    resultado = subtrair(10, 20)
    resultado = subtrair(10, 20)
    # resultado = somar(10, 20)

    

