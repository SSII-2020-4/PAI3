import os
from functools import wraps
from .client import cliente

from flask import request
from flask_restplus import Namespace, Resource, fields


api = Namespace(
    'message',
    description='Send message to a server over SSL 1.3'
)

client_message = api.model(
    'Request',
    {
        'user': fields.String(
            required=True,
            description="Username that identifies an user",
            help="Token cannot be blank."
        ),
        'password': fields.String(
            required=True,
            description="Password",
            help="Hash cannot be blank."
        ),
        'message': fields.String(
            required=True,
            description="Message to send to the server",
            help="Filename cannot be blank."
        )
    }
)


@api.route("/")
class ClientMessage(Resource):
    @api.doc(description="Send a message over SSL 1.3 to the server",
             responses={
                 200: "Message sent succesfully",
                 500: "Internal server error"
             })
    @api.expect(client_message)
    def post(self):
        return cliente(request.data)
