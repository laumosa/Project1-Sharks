import src.extraction as extract
import src.cleaning as clean
import src.visualization as viz


df = extract.open_df("attacks")
df_clean = clean.basic_cleaning_1(df)
df_clean_question_1 = clean.cleaning_question_1(df_clean)
df_clean_question_2 = clean.cleaning_question_2(df_clean)
df_clean_question_3 = clean.cleaning_question_3(df_clean)
viz.visualizing_question_1(df_clean_question_1, "graph_1")
viz.visualizing_question_2_a(df_clean_question_2, "graph_2")
viz.visualizing_question_2_b(df_clean_question_2, "graph_3")
viz.visualizing_question_3(df_clean_question_2, "graph_4")