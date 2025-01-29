from django.db.models import Q
import fireducks.pandas as pandas
from rest_framework import status
from .models import ChromosomeRegion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import ChromosomeRegionSerializer


class ChromosomeRegionUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        if "file" not in request.FILES:
            return Response(
                {"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES["file"]

        try:
            # Read TSV file
            df = pandas.read_csv(file, sep="\t", names=["chr", "start", "end"])
        except Exception as e:
            return Response(
                {"error": f"Invalid file format: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        results = []

        for _, row in df.iterrows():
            end_pos = row["end"]
            chr_name = row["chr"]
            start_pos = row["start"]

            # Find overlapping regions
            matching_regions = ChromosomeRegion.objects.filter(
                Q(chr=chr_name) & Q(start__lte=end_pos) & Q(end__gte=start_pos)
            )

            serialized_data = ChromosomeRegionSerializer(
                matching_regions, many=True
            ).data
            results.extend(serialized_data)

        return Response(results, status=status.HTTP_200_OK)
