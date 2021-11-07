import io
import pandas as pd
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .exceptions import InvalidDocumentError
from .serializers import DocumentSerializer, QuestionnaireSerializer
from .models import Document, Questionnaire


class DocumentView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def post(self, request, *args, **kwargs):
        if request.user:
            request.data["created_by"] = request.user.id
        return self.create(request, *args, **kwargs)


class DocumentUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def put(self, request, format="csv"):
        data = self.request.data.get('file')
        data_set = data.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        io_string = io.StringIO(data_set)

        csv_file = pd.read_csv(io_string, low_memory=False, header=None)

        if len(csv_file) > 1:
            raise InvalidDocumentError("More than 1 row found in the document.")
            
        columns = list(csv_file.columns.values)

        title, content = columns[0], columns[1]

        instances = [
            Document(
                title=row[title],
                content=row[content],
                created_by=request.user
            )

            for _, row in csv_file.iterrows()
        ]

        Document.objects.bulk_create(instances)

        return Response(status=204)


class QuestionnaireView(ListCreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def post(self, request, *args, **kwargs):
        if request.user:
            request.data["created_by"] = request.user.id
        return self.create(request, *args, **kwargs)


class QuestionnaireUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def put(self, request, format="csv"):
        data = self.request.data.get('file')
        data_set = data.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        io_string = io.StringIO(data_set)

        csv_file = pd.read_csv(io_string, low_memory=False)
        columns = list(csv_file.columns.values)

        question, answer = columns[0], columns[1]

        instances = [
            Questionnaire(
                question=row[question],
                answer=row[answer],
                created_by=request.user
            )

            for _, row in csv_file.iterrows()
        ]

        Questionnaire.objects.bulk_create(instances)

        return Response(status=204)
