from django.db import models


# Create your models here.
class ChromosomeRegion(models.Model):
    TYPE_CHOICES = [
        ("VaraDB_ATAC_TCGA", "VaraDB_ATAC_TCGA"),
        ("VaraDB_TFChipSEQ", "VaraDB_TFChipSEQ"),
        ("VaraDB_Promoter_TSS", "VaraDB_Promoter_TSS"),
        ("VaraDB_ATAC_CISTROME", "VaraDB_ATAC_CISTROME"),
        ("VaraDB_SuperEnhancer", "VaraDB_SuperEnhancer"),
        ("VaraDB_ChromatinState", "VaraDB_ChromatinState"),
        ("VaraDB_Enhancer_GROSeq", "VaraDB_Enhancer_GROSeq"),
        ("VaraDB_Enhancer_PROSeq", "VaraDB_Enhancer_PROSeq"),
        ("VaraDB_Disease_Enhancer", "VaraDB_Disease_Enhancer"),
        ("VaraDB_Enhancer_FANTOM5", "VaraDB_Enhancer_FANTOM5"),
        ("VaraDB_Typical_Enhancer", "VaraDB_Typical_Enhancer"),
        ("VaraDB_Promoter_ChromHMM", "VaraDB_Promoter_ChromHMM"),
        ("VaraDB_Validated_Enhancer_ENDB", "VaraDB_Validated_Enhancer_ENDB"),
        ("VaraDB_Validated_Enhancer_VISTA", "VaraDB_Validated_Enhancer_VISTA"),
        ("VaraDB_EnDisease_Disease_Enhancer", "VaraDB_EnDisease_Disease_Enhancer"),
        ("VaraDB_Enhancer_Target_Gene_FANTOM5", "VaraDB_Enhancer_Target_Gene_FANTOM5"),
        (
            "VaraDB_Enhancer_Target_Gene_ENCODEROADMap",
            "VaraDB_Enhancer_Target_Gene_ENCODEROADMap",
        ),
    ]

    chr = models.CharField(max_length=50, verbose_name="Chromosome")
    start = models.PositiveIntegerField(verbose_name="Start Position")
    end = models.PositiveIntegerField(verbose_name="End Position")
    type = models.CharField(
        max_length=100, verbose_name="Region Type", choices=TYPE_CHOICES
    )

    class Meta:
        verbose_name = "Chromosome Region"
        verbose_name_plural = "Chromosome Regions"
        ordering = ["chr", "start"]

    def __str__(self):
        return f"{self.chr}:{self.start}-{self.end} ({self.type})"


class VaraDB_TFChipSeq(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion", on_delete=models.CASCADE, related_name="varadb_tf_chipseq"
    )
    source = models.CharField(max_length=100, verbose_name="Source")
    tf = models.CharField(max_length=100, verbose_name="Transcription Factor")
    tf_class = models.CharField(
        max_length=100, verbose_name="Transcription Factor Class"
    )
    biosample_type = models.CharField(max_length=100, verbose_name="Biosample Type")
    biosample_name = models.CharField(max_length=100, verbose_name="Biosample Name")

    class Meta:
        verbose_name = "TF ChIP-seq Data"
        verbose_name_plural = "TF ChIP-seq Data"


class VaraDB_Promoter_ChromHMM(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_promoter_chrohmm",
    )
    from_state = models.CharField(max_length=100)
    epigenome_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Promoter ChromHMM"
        verbose_name_plural = "Promoter ChromHMM"


class VaraDB_Promoter_TSS(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_promoter_tss",
    )
    strand = models.CharField(max_length=100)
    gene_name = models.CharField(max_length=100)
    gene_id = models.CharField(max_length=100)
    gene_type = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Promoter Transcription Start Site (TSS)"
        verbose_name_plural = "Promoter Transcription Start Site (TSS)"


class VaraDB_SuperEnhancer(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_superenhancer",
    )
    rank = models.IntegerField()
    element = models.IntegerField()
    common_snp = models.IntegerField()
    eqtl = models.IntegerField()
    risk_snp = models.IntegerField()
    tfbs = models.IntegerField()
    crisps_cas9_target_sites = models.IntegerField()
    case_value = models.FloatField()
    control_value = models.FloatField()
    overlap_gene = models.TextField()
    proximal_gene = models.TextField()
    closest_gene = models.TextField()
    closest_active_gene = models.TextField()
    data_sources = models.TextField()
    biosample_type = models.CharField(max_length=255)
    tissue_type = models.CharField(max_length=255)
    biosample_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "SuperEnhancer"
        verbose_name_plural = "SuperEnhancer"


class VaraDB_ChromatinState(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_chromatin_state",
    )
    from_state = models.CharField(max_length=100)
    epigenome_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Chromatin State"
        verbose_name_plural = "Chromatin State"


class VaraDB_Enhancer_GROSeq(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_enhancer_groseq",
    )
    associated_gene_4dgenome = models.TextField(
        verbose_name="Associated Gene - 4D Genome"
    )
    detection_method = models.CharField(max_length=255, verbose_name="Detection Method")
    closest_gene = models.CharField(max_length=255, verbose_name="Closest Gene")
    cell_tissue = models.CharField(max_length=255, verbose_name="Cell/Tissue")
    series = models.CharField(max_length=255, verbose_name="Series")

    class Meta:
        verbose_name = "HACEER Active Enhancer GROSeq"
        verbose_name_plural = "HACEER Active Enhancer GROSeq"


class VaraDB_Enhancer_PROSeq(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_enhancer_proseq",
    )
    associated_gene_4dgenome = models.TextField(
        verbose_name="Associated Gene - 4D Genome"
    )
    detection_method = models.CharField(max_length=255, verbose_name="Detection Method")
    closest_gene = models.CharField(max_length=255, verbose_name="Closest Gene")
    cell_tissue = models.CharField(max_length=255, verbose_name="Cell/Tissue")
    series = models.CharField(max_length=255, verbose_name="Series")

    class Meta:
        verbose_name = "HACEER Active Enhancer PROSeq"
        verbose_name_plural = "HACEER Active Enhancer PROSeq"


class VaraDB_Enhancer_FANTOM5(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_enhancer_fantom5",
    )
    sample_id = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Active Enhancer FANTOM5"
        verbose_name_plural = "Active Enhancer FANTOM5"


class VaraDB_Disease_Enhancer(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_disease_enhancer",
    )
    target_gene = models.CharField(max_length=100)
    disease_type = models.TextField()

    class Meta:
        verbose_name = "Disease Enhancer"
        verbose_name_plural = "Disease Enhancer"


class VaraDB_EnDisease_Disease_Enhancer(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_endisease_disease_enhancer",
    )
    target_gene = models.CharField(max_length=100)
    disease_type = models.TextField()
    pubmed = models.CharField(max_length=100)

    class Meta:
        verbose_name = "EnDisease Disease Enhancer"
        verbose_name_plural = "EnDisease Disease Enhancer"


class VaraDB_Typical_Enhancer(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_typical_enhancer",
    )
    data_sources = models.CharField(max_length=100)
    biosample_type = models.TextField()
    tissue_type = models.CharField(max_length=100)
    biosample_name = models.CharField(max_length=100)
    rank = models.IntegerField()
    num_constituents = models.IntegerField()
    size_constituents = models.IntegerField()
    case_value = models.FloatField()
    control_value = models.FloatField()

    class Meta:
        verbose_name = "Typical Enhancer"
        verbose_name_plural = "Typical Enhancer"


class VaraDB_Validated_Enhancer_ENDB(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_validated_enhancer_endb",
    )
    enhancer_id = models.CharField(max_length=100)
    target_gene = models.TextField()
    disease = models.TextField()

    class Meta:
        verbose_name = "Validated Enhancer ENdb"
        verbose_name_plural = "Validated Enhancer ENdb"


class VaraDB_Validated_Enhancer_VISTA(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_validated_enhancer_vista",
    )
    vista_id = models.CharField(max_length=100)
    bracketing_gene = models.TextField()
    expression_pattern = models.TextField()

    class Meta:
        verbose_name = "Validated Enhancer VISTA"
        verbose_name_plural = "Validated Enhancer VISTA"


class VaraDB_ATAC_CISTROME(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_atac_cistrome",
    )
    gsm_id = models.CharField(max_length=100)
    biosample_type = models.TextField()
    biosample_name = models.TextField()

    class Meta:
        verbose_name = "ATAC Cistrome"
        verbose_name_plural = "ATAC Cistrome"


class VaraDB_ATAC_TCGA(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_atac_tcga",
    )
    cancer = models.CharField(max_length=100)
    score = models.FloatField()
    annotation = models.CharField(max_length=100)
    percent_gc = models.FloatField()
    percent_at = models.FloatField()

    class Meta:
        verbose_name = "ATAC TCGA"
        verbose_name_plural = "ATAC TCGA"


class VaraDB_DHS_ENCODE(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_dhs_encode",
    )
    signal_value = models.FloatField()
    biosample_term_name = models.CharField(max_length=100)
    biosample_type = models.TextField()
    biosample_treatments = models.TextField()

    class Meta:
        verbose_name = "DHS ENCODE"
        verbose_name_plural = "DHS ENCODE"


class VaraDB_Enhancer_Target_Gene_ENCODEROADMap(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_enhancer_target_gene_encoderoadmap",
    )
    gene = models.CharField(max_length=100)
    score = models.FloatField()
    sample_group = models.CharField(max_length=100)
    epigenome_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Enhancer Target Gene ENCODE Road Map"
        verbose_name_plural = "Enhancer Target Gene ENCODE Road Map"


class VaraDB_Enhancer_Target_Gene_FANTOM5(models.Model):
    chromosome_region = models.ForeignKey(
        "ChromosomeRegion",
        on_delete=models.CASCADE,
        related_name="varadb_enhancer_target_gene_fantom5",
    )
    gene = models.CharField(max_length=100)
    score = models.CharField(max_length=100)
    sample_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Enhancer Target Gene FANTOM5"
        verbose_name_plural = "Enhancer Target Gene FANTOM5"
