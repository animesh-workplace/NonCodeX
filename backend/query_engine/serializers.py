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
        fields = "__all__"


class VaraDBPromoterChromHMMSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Promoter_ChromHMM
        fields = "__all__"


class VaraDBPromoterTSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Promoter_TSS
        fields = "__all__"


class VaraDBSuperEnhancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_SuperEnhancer
        fields = "__all__"


class VaraDBChromatinStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_ChromatinState
        fields = "__all__"


class VaraDBEnhancerGROSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Enhancer_GROSeq
        fields = "__all__"


class VaraDBEnhancerPROSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Enhancer_PROSeq
        fields = "__all__"


class VaraDBEnhancerFANTOM5Serializer(serializers.ModelSerializer):
    class Meta:
        model = VaraDB_Enhancer_FANTOM5
        fields = "__all__"


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
        fields = "__all__"
