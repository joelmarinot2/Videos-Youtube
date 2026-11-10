-- Panel de Archivos Inexplicables: tablas y permisos.
-- Pegar completo en Supabase -> SQL Editor -> Run. Se puede ejecutar mas de una vez sin dañar nada.

create table if not exists public.videos (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users (id) on delete cascade,
  titulo text not null default '',
  datos jsonb not null default '{}'::jsonb,
  creado timestamptz not null default now(),
  actualizado timestamptz not null default now()
);

create table if not exists public.perfil_canal (
  user_id uuid primary key default auth.uid() references auth.users (id) on delete cascade,
  datos jsonb not null default '{}'::jsonb,
  actualizado timestamptz not null default now()
);

create index if not exists videos_usuario_fecha on public.videos (user_id, actualizado desc);

-- Seguridad: cada persona solo puede ver y cambiar sus propias filas.
alter table public.videos enable row level security;
alter table public.perfil_canal enable row level security;

drop policy if exists "videos del dueño" on public.videos;
create policy "videos del dueño" on public.videos
  for all to authenticated
  using (user_id = (select auth.uid()))
  with check (user_id = (select auth.uid()));

drop policy if exists "perfil del dueño" on public.perfil_canal;
create policy "perfil del dueño" on public.perfil_canal
  for all to authenticated
  using (user_id = (select auth.uid()))
  with check (user_id = (select auth.uid()));
