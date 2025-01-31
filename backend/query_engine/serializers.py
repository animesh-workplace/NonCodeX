from rest_framework import serializers
from .models import (
    ChromosomeRegion,
    VaraDB_TFChipSeq,
    VaraDB_Promoter_TSS,
    VaraDB_SuperEnhancer,
    VaraDB_ChromatinState,
    VaraDB_Enhancer_GROSeq,
    VaraDB_Enhancer_PROSeq,
    VaraDB_Enhancer_FANTOM5,
    VaraDB_Promoter_ChromHMM,
)


class VaraDBTFChipSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_TFChipSeq
        exclude = ("id",)


class VaraDBPromoterChromHMMSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Promoter_ChromHMM
        exclude = ("id",)


class VaraDBPromoterTSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Promoter_TSS
        exclude = ("id",)


class VaraDBSuperEnhancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_SuperEnhancer
        exclude = ("id",)


class VaraDBChromatinStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_ChromatinState
        exclude = ("id",)


class VaraDBEnhancerGROSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Enhancer_GROSeq
        exclude = ("id",)


class VaraDBEnhancerPROSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Enhancer_PROSeq
        exclude = ("id",)


class VaraDBEnhancerFANTOM5Serializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Enhancer_FANTOM5
        exclude = ("id",)


class ChromosomeRegionSerializer(serializers.ModelSerializer):
    varadb_tf_chipseq = VaraDBTFChipSeqSerializer(many=True, read_only=True)
    varadb_promoter_chrohmm = VaraDBPromoterChromHMMSerializer(
        many=True, read_only=True
    )
    varadb_promoter_tss = VaraDBPromoterTSSSerializer(many=True, read_only=True)
    varadb_superenhancer = VaraDBSuperEnhancerSerializer(many=True, read_only=True)
    varadb_chromatin_state = VaraDBChromatinStateSerializer(many=True, read_only=True)
    varadb_enhancer_groseq = VaraDBEnhancerGROSeqSerializer(many=True, read_only=True)
    varadb_enhancer_proseq = VaraDBEnhancerPROSeqSerializer(many=True, read_only=True)
    varadb_enhancer_fantom5 = VaraDBEnhancerFANTOM5Serializer(many=True, read_only=True)

    class Meta:
        model = ChromosomeRegion
        exclude = ("id",)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Extract base fields
        base_data = {
            "chr": data.pop("chr", None),
            "end": data.pop("end", None),
            "type": data.pop("type", None),
            "start": data.pop("start", None),
        }

        # Merge all related fields into a single list
        merged_data = []
        for key in [
            "varadb_tf_chipseq",
            "varadb_promoter_chrohmm",
            "varadb_promoter_tss",
            "varadb_superenhancer",
            "varadb_chromatin_state",
            "varadb_enhancer_groseq",
            "varadb_enhancer_proseq",
            "varadb_enhancer_fantom5",
        ]:
            if data[key]:  # Only include non-empty values
                merged_data.extend(data[key])

        # If only one related item exists, return a merged object
        if len(merged_data) == 1:
            return {**base_data, **merged_data[0]}

        # If multiple related items exist, return an array
        return [{**base_data, **item} for item in merged_data]
