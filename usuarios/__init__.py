{% extends "bases/base.html" %}
{% load static %}

{% block 'head' %}

   

{% endblock 'head' %}



{% block 'conteudo' %}
    <br>
    <br>
    <div class="container">
        <h3 class="font-destaque">Cadastre-se</h3>

        <div class="row">
            <div class="col-md-3" style="text-align: center">
                <img src="" alt="">
                <h3>VitaL</h3>
            </div>

            <div class="col-md-9">
                <form action="" method="POST">
                <label>Primeiro nome</label>
                <br>
                <input type="text" class="input-default" name="primeiro_nome">
                <br>
                <br>
                <label>Último nome</label>
                <br>
                <input type="text" class="input-default" name="ultimo_nome">
            </div>
        </div>

        <div class="row">
            <div class="col-md-4">
                <label>Username</label>
                <br>
                <input type="text" class="input-default w100" name="username">
                <br>
                <br>
                <label>Senha</label>
                <br>
                <input type="text" class="input-default w100" name="senha">
            </div>

            <div class="col-md-4">
                <label>E-mail</label>
                <br>
                <input type="text" class="input-default w100" name="email">
                <br>
                <br>
                <label>Confirmar senha</label>
                <br>
                <input type="text" class="input-default w100" name="confirmar_senha">
            </div>
            
        </div>
        <br>
        <input type="submit" class="btn-default">
    </form>
    </div>
{% endblock %}