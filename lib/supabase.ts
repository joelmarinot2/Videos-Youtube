import { createClient, type SupabaseClient } from "@supabase/supabase-js";

const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
const clave = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

// Si faltan las dos variables, el panel funciona en modo demostracion (guarda en el navegador).
export const supabase: SupabaseClient | null = url && clave ? createClient(url, clave) : null;
export const MODO_DEMO = supabase === null;
