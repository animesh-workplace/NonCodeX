from django.db import models


# Create your models here.
class ChromosomeRegion(models.Model):
    TYPE_CHOICES = [
        ("VaraDB_TFChipSEQ", "VaraDB_TFChipSEQ"),
        ("VaraDB_Promoter_TSS", "VaraDB_Promoter_TSS"),
        ("VaraDB_SuperEnhancer", "VaraDB_SuperEnhancer"),
        ("VaraDB_ChromatinState", "VaraDB_ChromatinState"),
        ("VaraDB_Enhancer_GROSeq", "VaraDB_Enhancer_GROSeq"),
        ("VaraDB_Enhancer_PROSeq", "VaraDB_Enhancer_PROSeq"),
        ("VaraDB_Enhancer_FANTOM5", "VaraDB_Enhancer_FANTOM5"),
        ("VaraDB_Promoter_ChromHMM", "VaraDB_Promoter_ChromHMM"),
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
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name = "Active Enhancer FANTOM5"
        verbose_name_plural = "Active Enhancer FANTOM5"
