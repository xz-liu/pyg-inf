# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inference_pb2 as inference__pb2


class InferenceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Inference = channel.unary_unary(
            '/Inference/Inference',
            request_serializer=inference__pb2.Inquiry.SerializeToString,
            response_deserializer=inference__pb2.Result.FromString,
        )
        self.StreamingInference = channel.stream_stream(
            '/Inference/StreamingInference',
            request_serializer=inference__pb2.SeedNode.SerializeToString,
            response_deserializer=inference__pb2.Result.FromString,
        )
        self.SetFixedBatchProperty = channel.unary_unary(
            '/Inference/SetFixedBatchProperty',
            request_serializer=inference__pb2.FixedBatchSizeProperty.SerializeToString,
            response_deserializer=inference__pb2.StatusCode.FromString,
        )
        self.StreamingFixedBatchInference = channel.stream_stream(
            '/Inference/StreamingFixedBatchInference',
            request_serializer=inference__pb2.SeedNode.SerializeToString,
            response_deserializer=inference__pb2.Result.FromString,
        )
        self.SetDynamicBatchProperty = channel.unary_unary(
            '/Inference/SetDynamicBatchProperty',
            request_serializer=inference__pb2.DynamicBatchSizeProperty.SerializeToString,
            response_deserializer=inference__pb2.StatusCode.FromString,
        )
        self.StreamingDynamicBatchInference = channel.stream_stream(
            '/Inference/StreamingDynamicBatchInference',
            request_serializer=inference__pb2.SeedNode.SerializeToString,
            response_deserializer=inference__pb2.Result.FromString,
        )
        self.StreamingInferenceByLabel = channel.stream_stream(
            '/Inference/StreamingInferenceByLabel',
            request_serializer=inference__pb2.SeedNodeLabel.SerializeToString,
            response_deserializer=inference__pb2.Result.FromString,
        )


class InferenceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Inference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingInference(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetFixedBatchProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingFixedBatchInference(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDynamicBatchProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingDynamicBatchInference(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingInferenceByLabel(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InferenceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Inference': grpc.unary_unary_rpc_method_handler(
            servicer.Inference,
            request_deserializer=inference__pb2.Inquiry.FromString,
            response_serializer=inference__pb2.Result.SerializeToString,
        ),
        'StreamingInference': grpc.stream_stream_rpc_method_handler(
            servicer.StreamingInference,
            request_deserializer=inference__pb2.SeedNode.FromString,
            response_serializer=inference__pb2.Result.SerializeToString,
        ),
        'SetFixedBatchProperty': grpc.unary_unary_rpc_method_handler(
            servicer.SetFixedBatchProperty,
            request_deserializer=inference__pb2.FixedBatchSizeProperty.FromString,
            response_serializer=inference__pb2.StatusCode.SerializeToString,
        ),
        'StreamingFixedBatchInference': grpc.stream_stream_rpc_method_handler(
            servicer.StreamingFixedBatchInference,
            request_deserializer=inference__pb2.SeedNode.FromString,
            response_serializer=inference__pb2.Result.SerializeToString,
        ),
        'SetDynamicBatchProperty': grpc.unary_unary_rpc_method_handler(
            servicer.SetDynamicBatchProperty,
            request_deserializer=inference__pb2.DynamicBatchSizeProperty.FromString,
            response_serializer=inference__pb2.StatusCode.SerializeToString,
        ),
        'StreamingDynamicBatchInference': grpc.stream_stream_rpc_method_handler(
            servicer.StreamingDynamicBatchInference,
            request_deserializer=inference__pb2.SeedNode.FromString,
            response_serializer=inference__pb2.Result.SerializeToString,
        ),
        'StreamingInferenceByLabel': grpc.stream_stream_rpc_method_handler(
            servicer.StreamingInferenceByLabel,
            request_deserializer=inference__pb2.SeedNodeLabel.FromString,
            response_serializer=inference__pb2.Result.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Inference', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Inference(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Inference(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inference/Inference',
                                             inference__pb2.Inquiry.SerializeToString,
                                             inference__pb2.Result.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingInference(request_iterator,
                           target,
                           options=(),
                           channel_credentials=None,
                           call_credentials=None,
                           insecure=False,
                           compression=None,
                           wait_for_ready=None,
                           timeout=None,
                           metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Inference/StreamingInference',
                                               inference__pb2.SeedNode.SerializeToString,
                                               inference__pb2.Result.FromString,
                                               options, channel_credentials,
                                               insecure, call_credentials, compression, wait_for_ready, timeout,
                                               metadata)

    @staticmethod
    def SetFixedBatchProperty(request,
                              target,
                              options=(),
                              channel_credentials=None,
                              call_credentials=None,
                              insecure=False,
                              compression=None,
                              wait_for_ready=None,
                              timeout=None,
                              metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inference/SetFixedBatchProperty',
                                             inference__pb2.FixedBatchSizeProperty.SerializeToString,
                                             inference__pb2.StatusCode.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingFixedBatchInference(request_iterator,
                                     target,
                                     options=(),
                                     channel_credentials=None,
                                     call_credentials=None,
                                     insecure=False,
                                     compression=None,
                                     wait_for_ready=None,
                                     timeout=None,
                                     metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Inference/StreamingFixedBatchInference',
                                               inference__pb2.SeedNode.SerializeToString,
                                               inference__pb2.Result.FromString,
                                               options, channel_credentials,
                                               insecure, call_credentials, compression, wait_for_ready, timeout,
                                               metadata)

    @staticmethod
    def SetDynamicBatchProperty(request,
                                target,
                                options=(),
                                channel_credentials=None,
                                call_credentials=None,
                                insecure=False,
                                compression=None,
                                wait_for_ready=None,
                                timeout=None,
                                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Inference/SetDynamicBatchProperty',
                                             inference__pb2.DynamicBatchSizeProperty.SerializeToString,
                                             inference__pb2.StatusCode.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingDynamicBatchInference(request_iterator,
                                       target,
                                       options=(),
                                       channel_credentials=None,
                                       call_credentials=None,
                                       insecure=False,
                                       compression=None,
                                       wait_for_ready=None,
                                       timeout=None,
                                       metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Inference/StreamingDynamicBatchInference',
                                               inference__pb2.SeedNode.SerializeToString,
                                               inference__pb2.Result.FromString,
                                               options, channel_credentials,
                                               insecure, call_credentials, compression, wait_for_ready, timeout,
                                               metadata)

    @staticmethod
    def StreamingInferenceByLabel(request_iterator,
                                  target,
                                  options=(),
                                  channel_credentials=None,
                                  call_credentials=None,
                                  insecure=False,
                                  compression=None,
                                  wait_for_ready=None,
                                  timeout=None,
                                  metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Inference/StreamingInferenceByLabel',
                                               inference__pb2.SeedNodeLabel.SerializeToString,
                                               inference__pb2.Result.FromString,
                                               options, channel_credentials,
                                               insecure, call_credentials, compression, wait_for_ready, timeout,
                                               metadata)
