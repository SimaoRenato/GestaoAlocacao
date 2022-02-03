# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alocacao(models.Model):
    idalocacao = models.AutoField(db_column='idAlocacao', primary_key=True)  # Field name made lowercase.
    colaborador_matricula = models.ForeignKey('Colaborador', models.DO_NOTHING, db_column='Colaborador_Matricula')  # Field name made lowercase.
    id_projetos = models.ForeignKey('Projetos', models.DO_NOTHING, db_column='ID_Projetos')  # Field name made lowercase.
    horas = models.IntegerField(db_column='Horas')  # Field name made lowercase.
    mes_ano = models.DateField(db_column='Mes_Ano')  # Field name made lowercase.
    cenario_1 = models.CharField(max_length=45, db_collation='utf8_bin')
    cenario_2 = models.CharField(max_length=45, db_collation='utf8_bin')
    cenario_3 = models.CharField(max_length=45, db_collation='utf8_bin')
    tipoalocacao_idtipoalocacao = models.ForeignKey('Tipoalocacao', models.DO_NOTHING, db_column='tipoAlocacao_idtipoAlocacao')  # Field name made lowercase.



    class Meta:
        managed = True
        db_table = 'alocacao'


class Area(models.Model):
    idarea = models.IntegerField(primary_key=True)
    nome_area = models.CharField(db_column='Nome_Area', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.nome_area

    class Meta:
        managed = True
        db_table = 'area'
        ordering = ("nome_area","idarea")


class Colaborador(models.Model):
    matricula = models.IntegerField(primary_key=True)
    nomecolaborador = models.CharField(db_column='nomeColaborador', max_length=255)  # Field name made lowercase.
    ativo = models.CharField(max_length=25)
    id_equipe = models.ForeignKey('Equipe', models.DO_NOTHING, db_column='ID_Equipe')  # Field name made lowercase.
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='ID_Area')  # Field name made lowercase.
    id_contrato = models.ForeignKey('Contratos', models.DO_NOTHING, db_column='ID_Contrato')  # Field name made lowercase.
    #iniciocontrato = models.DateField(db_column='inicioContrato')
    #fimcontrato = models.DateField(db_column='fimContrato')


    def __str__(self):
        return self.nomecolaborador
        # return f"{self.matricula},{self.nomecolaborador},{self.id_contrato},{self.id_area}"

    class Meta:
        managed = True
        db_table = 'colaborador'
        ordering = ("matricula","nomecolaborador")


class Contratos(models.Model):
    idcontratos = models.IntegerField(db_column='idContratos', primary_key=True)  # Field name made lowercase.
    tipo_contrato = models.CharField(db_column='Tipo_contrato', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.tipo_contrato

    class Meta:
        managed = True
        db_table = 'contratos'


class Equipe(models.Model):
    idequipe = models.IntegerField(db_column='idEquipe', primary_key=True)  # Field name made lowercase.
    equipe = models.CharField(db_column='Equipe', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.equipe

    class Meta:
        managed = True
        db_table = 'equipe'


class Projetos(models.Model):
    idprojetos = models.IntegerField(db_column='idProjetos', primary_key=True)  # Field name made lowercase.
    nomeprojeto = models.CharField(db_column='NomeProjeto', max_length=45)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=45)  # Field name made lowercase.
    statusprojetos = models.CharField(db_column='StatusProjetos', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return self.nomeprojeto

    class Meta:
        managed = True
        db_table = 'projetos'


class Tipoalocacao(models.Model):
    idtipoalocacao = models.IntegerField(db_column='idtipoAlocacao', primary_key=True)  # Field name made lowercase.
    tipo_alocacao = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo_alocacao

    class Meta:
        managed = True
        db_table = 'tipoalocacao'


class Valorhora(models.Model):
    idvalorhora = models.AutoField(db_column='idValorHora', primary_key=True)  # Field name made lowercase.
    colaborador_matricula = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='Colaborador_Matricula')  # Field name made lowercase.
    valorhora = models.FloatField(db_column='valorHora')  # Field name made lowercase.
    vigenciainicio = models.DateField(db_column='vigenciaInicio')  # Field name made lowercase.
    vigenciafim = models.DateField(db_column='vigenciaFim')  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'valorhora'
