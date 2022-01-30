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
    colaborador_matrÝcula = models.ForeignKey('Colaborador', models.DO_NOTHING, db_column='Colaborador_MatrÝcula')  # Field name made lowercase.
    id_projetos = models.ForeignKey('Projetos', models.DO_NOTHING, db_column='ID_Projetos')  # Field name made lowercase.
    horas = models.IntegerField(db_column='Horas')  # Field name made lowercase.
    mes_ano = models.DateField(db_column='Mes/Ano')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cenßrio_1 = models.CharField(db_column='Cenßrio 1', max_length=45, db_collation='utf8_bin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cenßrio_2 = models.CharField(db_column='Cenßrio 2', max_length=45, db_collation='utf8_bin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cenßrio_3 = models.CharField(db_column='Cenßrio 3', max_length=45, db_collation='utf8_bin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_alocaþÒo_idtipo_alocaþÒo = models.ForeignKey('TipoAlocao', models.DO_NOTHING, db_column='tipo AlocaþÒo_idtipo AlocaþÒo')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'alocacao'

class Area(models.Model):
    idarea = models.IntegerField(primary_key=True)
    nome_area = models.CharField(db_column='Nome_Area', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Colaborador(models.Model):
    matrÝcula = models.IntegerField(db_column='MatrÝcula', primary_key=True)  # Field name made lowercase.
    nome_colaborador = models.CharField(db_column='Nome Colaborador', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ativo = models.CharField(db_column='Ativo', max_length=25)  # Field name made lowercase.
    id_equipe = models.ForeignKey('Equipe', models.DO_NOTHING, db_column='ID_Equipe')  # Field name made lowercase.
    id_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='ID_Area')  # Field name made lowercase.
    id_contrato = models.ForeignKey('Contratos', models.DO_NOTHING, db_column='ID_Contrato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaborador'


class Contratos(models.Model):
    idcontratos = models.IntegerField(db_column='idContratos', primary_key=True)  # Field name made lowercase.
    tipo_contrato = models.CharField(db_column='Tipo_contrato', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contratos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipe(models.Model):
    idequipe = models.IntegerField(db_column='idEquipe', primary_key=True)  # Field name made lowercase.
    equipe = models.CharField(db_column='Equipe', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipe'


class Projetos(models.Model):
    idprojetos = models.IntegerField(db_column='idProjetos', primary_key=True)  # Field name made lowercase.
    nome_projeto = models.CharField(db_column='Nome projeto', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    empresa = models.CharField(db_column='Empresa', max_length=45)  # Field name made lowercase.
    status_dos_projetos = models.CharField(db_column='Status dos projetos', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'projetos'


class TipoAlocao(models.Model):
    idtipo_alocaþÒo = models.IntegerField(db_column='idtipo AlocaþÒo', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_alocacao = models.CharField(db_column='Tipo_alocacao', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo alocaþÒo'


class ValorHora(models.Model):
    idvalor_hora = models.AutoField(db_column='idValor Hora', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    colaborador_matrÝcula = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='Colaborador_MatrÝcula')  # Field name made lowercase.
    valor_hora = models.FloatField(db_column='Valor/hora')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vigÛncia_inÝcio = models.DateField(db_column='VigÛncia InÝcio')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vigÛncia_fim = models.DateField(db_column='VigÛncia Fim')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'valor hora'
