# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mafia_pb2 as mafia__pb2


class MafiaStub(object):
    """Rooms and chats handlers
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Action = channel.unary_stream(
                '/mafia.Mafia/Action',
                request_serializer=mafia__pb2.ActionRequest.SerializeToString,
                response_deserializer=mafia__pb2.ActionResponse.FromString,
                )
        self.ChatStream = channel.unary_stream(
                '/mafia.Mafia/ChatStream',
                request_serializer=mafia__pb2.ChatStreamRequest.SerializeToString,
                response_deserializer=mafia__pb2.ChatStreamResponse.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/mafia.Mafia/SendMessage',
                request_serializer=mafia__pb2.SendMessageRequest.SerializeToString,
                response_deserializer=mafia__pb2.SendMessageResponse.FromString,
                )
        self.JoinRoom = channel.unary_unary(
                '/mafia.Mafia/JoinRoom',
                request_serializer=mafia__pb2.JoinRoomRequest.SerializeToString,
                response_deserializer=mafia__pb2.JoinRoomResponse.FromString,
                )
        self.CreateRoom = channel.unary_unary(
                '/mafia.Mafia/CreateRoom',
                request_serializer=mafia__pb2.CreateRoomRequest.SerializeToString,
                response_deserializer=mafia__pb2.CreateRoomResponse.FromString,
                )
        self.GetGameStatus = channel.unary_unary(
                '/mafia.Mafia/GetGameStatus',
                request_serializer=mafia__pb2.GetGameStatusRequest.SerializeToString,
                response_deserializer=mafia__pb2.GetGameStatusResponse.FromString,
                )
        self.GetPlayers = channel.unary_unary(
                '/mafia.Mafia/GetPlayers',
                request_serializer=mafia__pb2.GetPlayersRequest.SerializeToString,
                response_deserializer=mafia__pb2.GetPlayersResponse.FromString,
                )
        self.CheckUser = channel.unary_unary(
                '/mafia.Mafia/CheckUser',
                request_serializer=mafia__pb2.CheckUserRequest.SerializeToString,
                response_deserializer=mafia__pb2.CheckUserResponse.FromString,
                )
        self.KillPlayer = channel.unary_unary(
                '/mafia.Mafia/KillPlayer',
                request_serializer=mafia__pb2.KillPlayerRequest.SerializeToString,
                response_deserializer=mafia__pb2.KillPlayerResponse.FromString,
                )
        self.VotePaper = channel.unary_unary(
                '/mafia.Mafia/VotePaper',
                request_serializer=mafia__pb2.VotePaperRequest.SerializeToString,
                response_deserializer=mafia__pb2.VotePaperResponse.FromString,
                )
        self.GetPlayerUpdates = channel.unary_unary(
                '/mafia.Mafia/GetPlayerUpdates',
                request_serializer=mafia__pb2.GetPlayerUpdatesRequest.SerializeToString,
                response_deserializer=mafia__pb2.GetPlayerUpdatesResponse.FromString,
                )
        self.DayToNight = channel.unary_unary(
                '/mafia.Mafia/DayToNight',
                request_serializer=mafia__pb2.DayToNightRequest.SerializeToString,
                response_deserializer=mafia__pb2.DayToNightResponse.FromString,
                )
        self.NightToDay = channel.unary_unary(
                '/mafia.Mafia/NightToDay',
                request_serializer=mafia__pb2.NightToDayRequest.SerializeToString,
                response_deserializer=mafia__pb2.NightToDayResponse.FromString,
                )
        self.UserInfo = channel.unary_unary(
                '/mafia.Mafia/UserInfo',
                request_serializer=mafia__pb2.UserInfoRequest.SerializeToString,
                response_deserializer=mafia__pb2.UserInfoResponse.FromString,
                )
        self.ChangeUserInfo = channel.unary_unary(
                '/mafia.Mafia/ChangeUserInfo',
                request_serializer=mafia__pb2.ChangeUserInfoRequest.SerializeToString,
                response_deserializer=mafia__pb2.ChangeUserInfoResponse.FromString,
                )
        self.RoomUsers = channel.unary_unary(
                '/mafia.Mafia/RoomUsers',
                request_serializer=mafia__pb2.RoomUsersRequest.SerializeToString,
                response_deserializer=mafia__pb2.RoomUsersResponse.FromString,
                )
        self.SetAvatar = channel.unary_unary(
                '/mafia.Mafia/SetAvatar',
                request_serializer=mafia__pb2.SetAvatarRequest.SerializeToString,
                response_deserializer=mafia__pb2.SetAvatarResponse.FromString,
                )


class MafiaServicer(object):
    """Rooms and chats handlers
    """

    def Action(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChatStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRoom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGameStatus(self, request, context):
        """Game logic

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KillPlayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VotePaper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayerUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DayToNight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NightToDay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UserInfo(self, request, context):
        """Flask logic

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeUserInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RoomUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAvatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MafiaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Action': grpc.unary_stream_rpc_method_handler(
                    servicer.Action,
                    request_deserializer=mafia__pb2.ActionRequest.FromString,
                    response_serializer=mafia__pb2.ActionResponse.SerializeToString,
            ),
            'ChatStream': grpc.unary_stream_rpc_method_handler(
                    servicer.ChatStream,
                    request_deserializer=mafia__pb2.ChatStreamRequest.FromString,
                    response_serializer=mafia__pb2.ChatStreamResponse.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=mafia__pb2.SendMessageRequest.FromString,
                    response_serializer=mafia__pb2.SendMessageResponse.SerializeToString,
            ),
            'JoinRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinRoom,
                    request_deserializer=mafia__pb2.JoinRoomRequest.FromString,
                    response_serializer=mafia__pb2.JoinRoomResponse.SerializeToString,
            ),
            'CreateRoom': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRoom,
                    request_deserializer=mafia__pb2.CreateRoomRequest.FromString,
                    response_serializer=mafia__pb2.CreateRoomResponse.SerializeToString,
            ),
            'GetGameStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGameStatus,
                    request_deserializer=mafia__pb2.GetGameStatusRequest.FromString,
                    response_serializer=mafia__pb2.GetGameStatusResponse.SerializeToString,
            ),
            'GetPlayers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayers,
                    request_deserializer=mafia__pb2.GetPlayersRequest.FromString,
                    response_serializer=mafia__pb2.GetPlayersResponse.SerializeToString,
            ),
            'CheckUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckUser,
                    request_deserializer=mafia__pb2.CheckUserRequest.FromString,
                    response_serializer=mafia__pb2.CheckUserResponse.SerializeToString,
            ),
            'KillPlayer': grpc.unary_unary_rpc_method_handler(
                    servicer.KillPlayer,
                    request_deserializer=mafia__pb2.KillPlayerRequest.FromString,
                    response_serializer=mafia__pb2.KillPlayerResponse.SerializeToString,
            ),
            'VotePaper': grpc.unary_unary_rpc_method_handler(
                    servicer.VotePaper,
                    request_deserializer=mafia__pb2.VotePaperRequest.FromString,
                    response_serializer=mafia__pb2.VotePaperResponse.SerializeToString,
            ),
            'GetPlayerUpdates': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayerUpdates,
                    request_deserializer=mafia__pb2.GetPlayerUpdatesRequest.FromString,
                    response_serializer=mafia__pb2.GetPlayerUpdatesResponse.SerializeToString,
            ),
            'DayToNight': grpc.unary_unary_rpc_method_handler(
                    servicer.DayToNight,
                    request_deserializer=mafia__pb2.DayToNightRequest.FromString,
                    response_serializer=mafia__pb2.DayToNightResponse.SerializeToString,
            ),
            'NightToDay': grpc.unary_unary_rpc_method_handler(
                    servicer.NightToDay,
                    request_deserializer=mafia__pb2.NightToDayRequest.FromString,
                    response_serializer=mafia__pb2.NightToDayResponse.SerializeToString,
            ),
            'UserInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.UserInfo,
                    request_deserializer=mafia__pb2.UserInfoRequest.FromString,
                    response_serializer=mafia__pb2.UserInfoResponse.SerializeToString,
            ),
            'ChangeUserInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeUserInfo,
                    request_deserializer=mafia__pb2.ChangeUserInfoRequest.FromString,
                    response_serializer=mafia__pb2.ChangeUserInfoResponse.SerializeToString,
            ),
            'RoomUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.RoomUsers,
                    request_deserializer=mafia__pb2.RoomUsersRequest.FromString,
                    response_serializer=mafia__pb2.RoomUsersResponse.SerializeToString,
            ),
            'SetAvatar': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAvatar,
                    request_deserializer=mafia__pb2.SetAvatarRequest.FromString,
                    response_serializer=mafia__pb2.SetAvatarResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mafia.Mafia', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mafia(object):
    """Rooms and chats handlers
    """

    @staticmethod
    def Action(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mafia.Mafia/Action',
            mafia__pb2.ActionRequest.SerializeToString,
            mafia__pb2.ActionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChatStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mafia.Mafia/ChatStream',
            mafia__pb2.ChatStreamRequest.SerializeToString,
            mafia__pb2.ChatStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/SendMessage',
            mafia__pb2.SendMessageRequest.SerializeToString,
            mafia__pb2.SendMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/JoinRoom',
            mafia__pb2.JoinRoomRequest.SerializeToString,
            mafia__pb2.JoinRoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRoom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/CreateRoom',
            mafia__pb2.CreateRoomRequest.SerializeToString,
            mafia__pb2.CreateRoomResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGameStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/GetGameStatus',
            mafia__pb2.GetGameStatusRequest.SerializeToString,
            mafia__pb2.GetGameStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/GetPlayers',
            mafia__pb2.GetPlayersRequest.SerializeToString,
            mafia__pb2.GetPlayersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/CheckUser',
            mafia__pb2.CheckUserRequest.SerializeToString,
            mafia__pb2.CheckUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KillPlayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/KillPlayer',
            mafia__pb2.KillPlayerRequest.SerializeToString,
            mafia__pb2.KillPlayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VotePaper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/VotePaper',
            mafia__pb2.VotePaperRequest.SerializeToString,
            mafia__pb2.VotePaperResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlayerUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/GetPlayerUpdates',
            mafia__pb2.GetPlayerUpdatesRequest.SerializeToString,
            mafia__pb2.GetPlayerUpdatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DayToNight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/DayToNight',
            mafia__pb2.DayToNightRequest.SerializeToString,
            mafia__pb2.DayToNightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NightToDay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/NightToDay',
            mafia__pb2.NightToDayRequest.SerializeToString,
            mafia__pb2.NightToDayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UserInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/UserInfo',
            mafia__pb2.UserInfoRequest.SerializeToString,
            mafia__pb2.UserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeUserInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/ChangeUserInfo',
            mafia__pb2.ChangeUserInfoRequest.SerializeToString,
            mafia__pb2.ChangeUserInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RoomUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/RoomUsers',
            mafia__pb2.RoomUsersRequest.SerializeToString,
            mafia__pb2.RoomUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAvatar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafia.Mafia/SetAvatar',
            mafia__pb2.SetAvatarRequest.SerializeToString,
            mafia__pb2.SetAvatarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
