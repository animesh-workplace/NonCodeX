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
