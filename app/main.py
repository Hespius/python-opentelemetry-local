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
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)

# Método de contexto do trace com um decorator
def trace_context_method(span_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with trace.get_tracer(__name__).start_as_current_span(span_name):
                result = func(*args, **kwargs)
                return result
        return wrapper
    return decorator


# Função para realizar somas matemáticas
@trace_context_method("soma")
def somar(a, b):
    resultado = a + b
    return subtrair(resultado, 10)

@trace_context_method("sub")
def subtrair(a, b):
    return a - b

if __name__ == "__main__":
    resultado = somar(10, 20)
    resultado = somar(10, 20)
    resultado = somar(10, 20)
    resultado = subtrair(10, 20)
    resultado = subtrair(10, 20)
    resultado = somar(10, 20)
    print(f"Resultado da soma: {resultado}")

# Certifique-se de configurar o ambiente com as variáveis de ambiente necessárias para o console exporter.
