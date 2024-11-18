import streamlit as st
from supabase import create_client, Client 

# from st_supabase_connection import SupabaseConnection

# conn = st.connection("supabase", type=SupabaseConnection)
# rows = conn("*", table="mytable", ttl="10m").execute()

@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

@st.cache_resource(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()
rows = run_query()

for row in rows.data:
    st.write(f" {row['name']} has a : {row['pet']}")