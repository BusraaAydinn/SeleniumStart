PyTest Decorators

PyTest, Python'da testleri yazmak için kullanılan popüler bir kütüphanedir. PyTest, decoratorları kullanarak testleri daha kolay ve verimli hale getirmeyi sağlar.

Decoratorlar, bir fonksiyona veya sınıfa ek işlevsellik eklemek için kullanılan bir tasarım desenine dayanır. PyTest'te decoratorlar, testleri çalıştırma şeklini değiştirmek için kullanılabilir.

PyTest decoratorlarını kullanarak testlerinizi daha verimli hale getirebilirsiniz. Decoratorlar, testlerinizi daha kolay çalıştırmanıza, hata ayıklamanızı ve raporlamanızı sağlar.

PyTest'te Kullanılan Bazı Yaygın Decoratorlar


@pytest.mark.parametrize(): Bu decorator, bir test fonksiyonunu birden çok parametre ile çalıştırmanızı sağlar. Bu, aynı test kodunu farklı veri kümeleri üzerinde çalıştırmak için kullanışlıdır.

@pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])
def test_add(a, b):
    assert add(a, b) == a + b

-Bu kod, add() fonksiyonunu iki kez çalıştıracaktır: bir kez a=1 ve b=2 ile ve bir kez a=3 ve b=4 ile.


@pytest.mark.skip(): Bu decorator, bir test fonksiyonunun atlanması gerektiğini belirtir. Bu, testin henüz hazır olmadığı veya belirli bir durumda çalışmaması gerektiği durumlarda kullanışlıdır.

@pytest.mark.skipif(sys.version_info < (3, 6), reason="Requires Python 3.6 or later")
def test_new_feature():
    assert True

-Bu kod, sys.version_info'nın (3, 6)'dan küçük olduğu durumlarda test_new_feature() test fonksiyonunu atlayacaktır.


@pytest.mark.xfail(): Bu decorator, bir test fonksiyonunun başarısız olmasını beklediğinizi belirtir. Bu, bir hata düzeltmesi veya yeni bir özellik eklendikten sonra bir testin geçici olarak başarısız olmasını önlemek için kullanışlıdır.

@pytest.mark.xfail
def test_flaky_test():
    assert True

-Bu kod, test_flaky_test() test fonksiyonunun başarısız olmasını beklemektedir.


PyTest Decoratorlarını Kullanma

PyTest decoratorlarını kullanmak için, bir decorator'ü bir test fonksiyonu veya sınıfına atamanız yeterlidir. Örneğin, aşağıdaki kod, add() fonksiyonunu iki parametre ile çalıştırır:

@pytest.mark.parametrize("a,b", [(1, 2), (3, 4)])
def test_add(a, b):
    assert add(a, b) == a + b

-Bu kod, add() fonksiyonunu iki kez çalıştıracaktır: bir kez a=1 ve b=2 ile ve bir kez a=3 ve b=4 ile.


