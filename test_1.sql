PGDMP     2    !                {            Test_1    15.2    15.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16569    Test_1    DATABASE     {   CREATE DATABASE "Test_1" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
    DROP DATABASE "Test_1";
                postgres    false            �            1259    16606    persona    TABLE     �   CREATE TABLE public.persona (
    id_persona integer NOT NULL,
    nombre character varying(20),
    cedula character varying(20)
);
    DROP TABLE public.persona;
       public         heap    postgres    false            �          0    16606    persona 
   TABLE DATA           =   COPY public.persona (id_persona, nombre, cedula) FROM stdin;
    public          postgres    false    214   [       e           2606    16613    persona persona_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.persona
    ADD CONSTRAINT persona_pkey PRIMARY KEY (id_persona);
 >   ALTER TABLE ONLY public.persona DROP CONSTRAINT persona_pkey;
       public            postgres    false    214            �   [   x�3�t�K)J-�442�053���2��*M�
� ŀ�˘�7�$3�������Ē�(V���ilj�[ ��r���d������b���� �mE     