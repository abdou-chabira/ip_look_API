CREATE TABLE public.ip_abuse_report (
	abuse_report_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	ip_address varchar(50) NOT NULL,
	abusecategory int NOT NULL,
	created_dt timestamp NOT NULL,
	updated_dt timestamp NOT NULL
);