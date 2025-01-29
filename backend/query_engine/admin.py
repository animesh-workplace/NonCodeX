from django.contrib import admin
from .models import (
    ChromosomeRegion,
    VaraDB_TFChipSeq,
    VaraDB_Promoter_ChromHMM,
    VaraDB_Promoter_TSS,
    VaraDB_SuperEnhancer,
    VaraDB_ChromatinState,
    VaraDB_Enhancer_GROSeq,
    VaraDB_Enhancer_PROSeq,
    VaraDB_Enhancer_FANTOM5,
)


@admin.register(ChromosomeRegion)
class ChromosomeRegionAdmin(admin.ModelAdmin):
    list_display = ("chr", "start", "end", "type")
    list_filter = ("type", "chr")
    search_fields = ("chr", "type")


@admin.register(VaraDB_TFChipSeq)
class VaraDB_TFChipSeqAdmin(admin.ModelAdmin):
    list_display = (
        "chromosome_region",
        "tf",
        "tf_class",
        "biosample_type",
        "biosample_name",
    )
    list_filter = ("tf_class", "biosample_type")
    search_fields = ("tf", "biosample_name")


@admin.register(VaraDB_Promoter_ChromHMM)
class VaraDB_Promoter_ChromHMMAdmin(admin.ModelAdmin):
    list_display = ("chromosome_region", "from_state", "epigenome_id")
    list_filter = ("from_state",)
    search_fields = ("epigenome_id", "from_state")


@admin.register(VaraDB_Promoter_TSS)
class VaraDB_Promoter_TSSAdmin(admin.ModelAdmin):
    list_display = ("chromosome_region", "strand", "gene_name", "gene_id", "gene_type")
    list_filter = ("gene_type", "strand")
    search_fields = ("gene_name", "gene_id")


@admin.register(VaraDB_SuperEnhancer)
class VaraDB_SuperEnhancerAdmin(admin.ModelAdmin):
    list_display = (
        "chromosome_region",
        "rank",
        "biosample_type",
        "tissue_type",
        "biosample_name",
    )
    list_filter = ("biosample_type", "tissue_type")
    search_fields = ("biosample_name", "closest_gene", "overlap_gene")


@admin.register(VaraDB_ChromatinState)
class VaraDB_ChromatinStateAdmin(admin.ModelAdmin):
    list_display = ("chromosome_region", "from_state", "epigenome_id")
    list_filter = ("from_state",)
    search_fields = ("epigenome_id", "from_state")


@admin.register(VaraDB_Enhancer_GROSeq)
class VaraDB_Enhancer_GROSeqAdmin(admin.ModelAdmin):
    list_display = (
        "chromosome_region",
        "detection_method",
        "closest_gene",
        "cell_tissue",
        "series",
    )
    list_filter = ("detection_method", "cell_tissue")
    search_fields = ("closest_gene", "associated_gene_4dgenome")


@admin.register(VaraDB_Enhancer_PROSeq)
class VaraDB_Enhancer_PROSeqAdmin(admin.ModelAdmin):
    list_display = (
        "chromosome_region",
        "detection_method",
        "closest_gene",
        "cell_tissue",
        "series",
    )
    list_filter = ("detection_method", "cell_tissue")
    search_fields = ("closest_gene", "associated_gene_4dgenome")


@admin.register(VaraDB_Enhancer_FANTOM5)
class VaraDB_Enhancer_FANTOM5Admin(admin.ModelAdmin):
    list_display = ("chromosome_region", "sample_id", "description")
    search_fields = ("sample_id", "description")
