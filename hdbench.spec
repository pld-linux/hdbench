Summary:	A benchmark software like HDBENCH
Summary(ja):	HDBENCH �饤���ʥ٥���ޡ������ե�
Summary(pl):	Hdbench narz�dzie do benchmark�w CPU, Video i HDD
Name:		hdbench
Version:	0.14.0
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://download.vector.co.jp/pack/unix/hardware/bench/%{name}-%{version}.tar.gz
# Source0-md5:	98984d51811ee95ed00ae07728d3f37e
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2.0

%description
HDBENCH clone is a benchmark software like HDBENCH which is the most
famous benchmark software for Windows in Japan. With this tool You can
benchmark Your CPU, Video Card and HDD.

%description -l pl
Pakiet zawiera narzedzie pozwalaj�ce zmierzy� wydajno�� procesora,
karty video, i dysku. Hdbench jest klonem narz�dzia HDBENCH
stworzonego dla system�w Windows.

%description -l ja
HDBENCH clone��Windows�ѥ٥���ޡ������եȤ����֡�HDBENCH�פ�UNIX��
�ܿ��������եȡ������ǤϤ���ޤ���ñ�˥桼�����󥿥ե������򿿻���������
��Ȥ�HDBENCH��������ʪ�Ǥ���

%prep

%setup -q

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_pixmapsdir},%{_docdir}/%{name}}

install pixmaps/*xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install src/hdbench $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,BUGS,ChangeLog,FAQ,README,RESULTS,THANKS,TODO,WANTED}
%lang(ja) %doc doc/{ALGORITHM,BUGS,ChangeLog,FAQ,README,TODO,WANTED}.jp
%doc doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*.xpm
